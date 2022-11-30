#!/usr/bin/python
# -*- coding: utf-8 -*-
from google.cloud import storage
from google.cloud import bigquery
import logging
import numpy as np
from datetime import datetime
from pytz import timezone
import pandas as pd
import os
import functions


# Function from KPI-KA cloud function


def trigger_gcs(event, context):
    # Retrieve GCS CSV file
    client = storage.Client()
    file_name = 'gs://' + event['bucket'] + '/' + event['name']

    # Create pandas dataframe from CSV
    df_csv = pd.read_csv(file_name, encoding='utf-8', sep=';')
    # Create a var with the first BU code
    first_bu_code = df_csv.bu_code[0]
    # Retrieve unique asset_id to Dataframe
    df1 = df_csv[['bu_code', 'asset_id', 'key_asset_code']]
    # Add csv line in error in the dataframe
    df1.insert(loc=0, column='CSV line Number',
               value=np.arange(1, len(df1) + 1) + 1)
    print('####### DF1 PRINT ########')
    print(df1)

    # Construct a BigQuery client object.
    client = bigquery.Client()
    # Retrieve bu_code,asset_id,key_asset_code  list for controls
    table_name = '`ake-actionable-product-data-dv.pim_customers_data.pim_hashed_tables`'
    sql = 'SELECT BU_Code as bu_code,key_asset_name as asset_id,code_key_asset as key_asset_code FROM ' + table_name + ' GROUP BY 1,2,3'
    df2 = client.query(sql).to_dataframe()
    print('####### DF2 PRINT ########')
    print(df2)

    # Left join indicates the number of left_only (aka: different from other column)
    merged_bu_code = pd.merge(
        df1, df2, on='bu_code', how='left', indicator=True)
    print('####### merged_bu_code ########')
    print(merged_bu_code)
    # Count number of bu_code errors
    anomaly_count_bu_code = len(
        merged_bu_code[merged_bu_code['_merge'] == 'left_only'])
    # Left join indicates the number of left_only (aka: different from other column)
    merged_key_asset_code = pd.merge(
        df1, df2, on='key_asset_code', how='left', indicator=True)
    print('####### merged_key_asset_code ########')
    print(merged_key_asset_code)
    # Count number of key_asset_code errors
    anomaly_count_key_asset_code = len(
        merged_key_asset_code[merged_key_asset_code['_merge'] == 'left_only'])

    # If there is anomaly for bu_code or key_asset_code
    if (anomaly_count_bu_code > 0) or (anomaly_count_key_asset_code > 0):
        # If errors come from bu_code
        if anomaly_count_bu_code > 0:
            # Retrieve merged values
            alert_bu_code = (
                merged_bu_code[merged_bu_code['_merge'] == 'left_only'])
            # Take only first 3 columns
            alert_bu_code = alert_bu_code.iloc[:, :4]
            # Transform dataframe to string removing index
            alert_bu_code = alert_bu_code.to_string(header=False, index=False)
        # Else default mail error string
        else:
            alert_bu_code = 'There is no alert_bu_code to display'
        if anomaly_count_key_asset_code > 0:
            # Retrieve merged values
            alert_key_asset_code = (
                merged_key_asset_code[merged_key_asset_code['_merge'] == 'left_only'])
            print(alert_key_asset_code)
            # Take only first 3 columns
            alert_key_asset_code = alert_key_asset_code.iloc[:, :4]
            # Transform dataframe to string removing index
            alert_key_asset_code = alert_key_asset_code.to_string(
                header=False, index=False)
        # Else default mail error string
        else:
            alert_key_asset_code = 'There is no alert_key_asset_code to display'
        # Logging in function log
        logging.info('===================== ERROR =====================')
        # Send the file to error bucket
        functions.mv_blob(event['bucket'], event['name'],
                          os.environ['ERROR_BUCKET'], event['name'])
        # Construct the error path for mail subject
        error_path = os.environ['ERROR_BUCKET'] + '/' + event['name']
        # Send mail retrieving errors
        functions.send_email(alert_bu_code, alert_key_asset_code, error_path)

    # Upload in the right bucket if controls are fine.
    else:
        # Retrieve
        # Replace with right asset_names
        df_csv['asset_id'] = df_csv['key_asset_code'].map(df2.set_index('key_asset_code')['asset_id'])
        df_csv.to_csv(file_name, encoding='utf-8', sep=';', index=False)
        # Logging in function log
        logging.info('===================== UPLOAD to target bucket =====================')
        # Workaround PROD / PRD
        if 'PROD' in os.environ['ENV']:
            os.environ['ENV'] = 'PRD'
        # Query to map buckets with BU_code in the CSV file
        table_name = '`' + os.environ['GCP_PROJECT_ID'] + '.' + \
                     os.environ['DATASET'] + '.9_KPI_KA_Bucket_Upload`'
        sql = 'SELECT BU,' + os.environ['ENV'] + '_Bucket,Zone FROM ' + \
              table_name + ' WHERE BU = "' + first_bu_code + '" LIMIT 1'
        df3 = client.query(sql).to_dataframe()
        # Name of target bucket
        bucket_value = df3[os.environ['ENV'] + '_Bucket'].values[0]
        # Retrieve Code Zone to format file destination name
        zone_value = df3['Zone'].values[0]
        # Construct future destination file name
        paris = timezone('Europe/Paris')
        target_file_name = 'KA_' + zone_value + '_' + \
                           datetime.now(paris).strftime('%Y/%m/%d %H:%M:%S') + '.csv'
        # Move and rename the file with good format for cloud composer ingestion.
        # Cloud composer ingestion
        functions.mv_blob(event['bucket'], event['name'],
                          bucket_value, datetime.now(paris).strftime('%Y/%m/%d') + '/' + target_file_name)

    logging.info(f'check the results in the logs')