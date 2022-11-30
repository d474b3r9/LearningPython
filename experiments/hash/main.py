import pandas as pd
from google.cloud import bigquery
from functions import generate_hash_table
from functions import hash_to_hashes
from datetime import datetime
from pytz import timezone

# input vars
min = 0
max = 72057594037927935
n_buckets = 5
# retrieve actual time
paris = timezone('Europe/Paris')
launch_time = datetime.now(paris).strftime('%Y/%m/%d %H:%M:%S')

### PREPARE ENV ###
# TODO HAG: create the table if not exists in DBT
# Create the table in python (workaround waiting DBT job) column timestamp + status (removed, updated)
# TODO HAG: input table to to get genericaly
input_file = ('bquxjob_2c1e9bb8_1849ada8591.csv')

### RETRIEVE AND ENRICH DATA LOCALY ###
# Retrieve client list / parse it generating immutable hash in a new column table
# TODO JCA : try catch log
df_list_clients = pd.read_csv(input_file)
df_list_clients['hash_id'] = df_list_clients.apply(lambda x: hash_to_hashes(str(tuple(x))), axis=1)

# Enrich the table cutting in bins with similar weight
hash_table = (generate_hash_table(min, max, n_buckets))
bins = hash_table[0]
labels = hash_table[1]
df_list_clients['bin'] = pd.cut(df_list_clients['hash_id'], bins=bins, labels=labels, include_lowest=True)
df_list_clients['tstp'] = launch_time
print(df_list_clients)

# TODO JCA drop it after tests print(df_list_clients) to erase after
df_list_clients.to_csv('test.csv', encoding='utf-8', sep=';')

### RETRIEVE AND UPDATE DATA BQ ###
# TODO JCA: read existing to BQ
# Construct a BigQuery client object
client = bigquery.Client()
# Retrieve bu_code,asset_id,key_asset_code  list for controls
table_name = '`ake-actionable-product-data-dv.dbt_JCA.bvxcbcxvbvc`'
# table_name = '`ake-actionable-product-data-dv.pim_customers_data.pim_hashed_tables`'
sql = 'SELECT client_id,hash_id,bin,tstp FROM ' + table_name
df_source = client.query(sql).to_dataframe()
# TODO JCA: test if less clients in the file than in table last period (seems impossible)
print('####### DF2 PRINT ########')
print(df_source)

# Compare data to existing

# Left join if doesn't exists
merged_hash = pd.merge(
    df_list_clients, df_source, on='hash_id', how='left', indicator=True, suffixes=('', '_y'))
# merge left only (new hashs)
new_hash = merged_hash.loc[merged_hash['_merge'] == 'left_only', :]
# removing merge columns
new_hash = merged_hash.iloc[:, :4]
# enrich with date & status new
new_hash['status'] = 'new'
print(new_hash.dtypes)
print('####### merged_hash ########')
print(new_hash)
print(new_hash.dtypes)
# Count number of new hashs
new_hash_count = len(
merged_hash[merged_hash['_merge'] == 'left_only'])
new_hash_count['client_id'].dtypes
    # .astype(str)
# new_hash_count.astype({'bin': 'int64'})
# new_hash_count.astype({'tstp': 'date'})
# new_hash_count.astype({'status': 'string'})


print('####### update hash count ########')
print(new_hash_count.dtypes)
# Columns: [client_id, hash_id, bin, tstp]
# Index: []
# client_id      object
# hash_id        uint64
# bin          category
# tstp           object
# status         object

# Retrieve merged values
# alert_bu_code = (
#     merged_hash[merged_hash['_merge'] == 'left_only'])
# # Take only first 3 columns
# alert_bu_code = alert_bu_code.iloc[:, :4]
# # Transform dataframe to string removing index
# alert_bu_code = alert_bu_code.to_string(header=False, index=False)

# write to BQ

# TODO JCA: add a timestamp at code begin and insert it in BQ for each modification + suppression + new




# launch_time

# TODO JCA: calculate diff by hash

# TODO JCA: update in BQ by hash

# TODO JCA: when you update, create a copy _OLD of table replacing last one (truncate ?)

# TODO HAG: read from this table to regenerate files by buckets

# TODO HAG : integration script

# TODO HAG + JCA : Refacto whole code
# refacto PEP8
# testing ???
# fix libs + venv

# return client split by bins
print(f' ')
print(f'You can find bucket split below :')
print(f'=================================')
print(df_list_clients['bin'].value_counts())


# python hash
# https://realpython.com/python-hash-table/
# python hash size:
# https://stackoverflow.com/questions/66526775/maximum-minimum-value-returned-by-pythons-hash-function
