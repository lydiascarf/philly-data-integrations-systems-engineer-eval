import pandas as pd
import requests
import urllib.parse

download_path = '311_requests.csv'
service_requests_df = pd.read_csv(download_path)
l_and_i_requests_df = service_requests_df.query("agency_responsible == 'License & Inspections'").sample(n=10)

def request_opa_account_number(address):
    if not isinstance(address, str):
        return ''
    safe_query_string = urllib.parse.quote(address)
    url = f'https://api.phila.gov/ais/v2/search/{safe_query_string}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('features',[{}])[0].get('properties',{}).get('opa_account_num', '')
    else:
        return ''

l_and_i_requests_df['opa_account_num'] = l_and_i_requests_df['address'].apply(request_opa_account_number)
print(l_and_i_requests_df)
