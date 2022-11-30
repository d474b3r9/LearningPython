#!/usr/bin/python
# -*- coding: utf-8 -*-
from google.cloud import secretmanager
from google.cloud import storage
import os
import requests
import logging
import jinja2
from jinja2 import select_autoescape
import json

# Function to move file from a bucket to another


def mv_blob(bucket_name, file_name, new_bucket_name, target_file_name):

    # construct a storage client
    storage_client = storage.Client()
    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(file_name)
    destination_bucket = storage_client.bucket(new_bucket_name)

    # copy to new destination
    source_bucket.copy_blob(
        source_blob, destination_bucket, target_file_name)
    # delete in old destination
    source_blob.delete()
    logging.info(
        f'File moved from {bucket_name}/{file_name} to {destination_bucket}/{target_file_name}')

# Function to retrieve secrets from GCP


def get_secured_settings(secret_id):

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()
    # Build the resource name of the secret version.
    name = f'projects/gbl-ist-ve-hubgradehub/secrets/{secret_id}/versions/latest'
    # Access the secret version.
    response = client.access_secret_version(request={'name': name})
    # Return the secret payload.
    payload = response.payload.data.decode('UTF-8')
    return payload

# Function json.dumps


def tojson(value):
    return json.dumps(value)

# Function to send mails using retarus API


def send_email(alerte_bu_code, alert_key_asset_code, error_path):

    # separate_email to true will send a separate mail for each person in the mailing list
    separate_email = False
    # Configure Jinja2 setting the jinja root folder
    JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'retarus')),
                                   trim_blocks=True,
                                   lstrip_blocks=True,
                                   autoescape=select_autoescape(['html']))
    JINJA_ENV.filters['tojson'] = tojson
    # Configure content in the HTML mail
    content = ('BU_CODE in error: \n' + alerte_bu_code +
               '\n \nkey_asset_code in error: \n' + alert_key_asset_code)
    # Read html template
    email_template = JINJA_ENV.get_template('email.html')
    # Create an html body
    html_body = email_template.render(content=content,
                                      sender=os.environ['EMAIL_FROM_ADDRESS']
                                      )
    # Parse the retarus json file
    email_api_template = JINJA_ENV.get_template('retarus.json')
    # Construct retarus request
    email_api_body = email_api_template.render(
        subject='KPI-KA loading errors ' + error_path,
        body=html_body,
        to=['jonathan.cattelain.ext@veolia.com',
            'gbl.bsp.key-asset-kpi-group.int.groups@veolia.com'
            ],
        from_address=os.environ['EMAIL_FROM_ADDRESS'],
        cc=[''],
        separate_email=separate_email
    )
    # Retrieve retarus secrects from GCP secret manager
    api_user = get_secured_settings('retarus_user')
    api_password = get_secured_settings('retarus_password')

    # POST retarus request
    api_resp = requests.post(os.environ['EMAIL_PROVIDER_URL'],
                             data=email_api_body,
                             auth=(api_user, api_password))
    # retrieve response in case of failure
    api_response = api_resp.json()
    email_state = api_response['meta']['state']
    # retarus requests return
    if api_resp.status_code == requests.codes.ok:
        api_response = api_resp.json()
        email_state = api_response['meta']['state']
        if email_state and email_state['type'] == 'ACCEPTED':
            return logging.info('Return code 201')
        else:
            logging.error('Error code 500 see the retarus return below: \n')
            logging.error(api_response)
            logging.error(email_state)
    else:
        logging.error('Error code 500 see the retarus return below: \n')
        logging.error(api_response)
        logging.error(email_state)