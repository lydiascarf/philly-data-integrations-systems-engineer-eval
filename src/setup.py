import os
import pandas as pd
import requests
import urllib.parse

def get_service_requests():
    df = None
    download_path = 'service_requests.csv'
    if os.path.exists(download_path):
        print('Cached service requests csv found')
        df = pd.read_csv(download_path)
    else:
        print('Downloading service requests csv')
        url = "https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20FROM%20public_cases_fc%20WHERE%20requested_datetime%20%3E=%20%272025-01-01%27%20AND%20requested_datetime%20%3C%20%272026-01-01%27"
        df = pd.read_csv(url)
        df.to_csv(download_path, index=False)
    return df

def get_violations():
    df = None
    download_path = 'violations.csv'
    if os.path.exists(download_path):
        print('Cached violations csv found')
        df = pd.read_csv(download_path)
    else:
        print('Downloading violations csv')
        url = "https://phl.carto.com/api/v2/sql?&filename=violations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20violations%20WHERE%20violationdate%20%3E=%20%272019-01-01%27"
        df = pd.read_csv(url, dtype={'opa_account_num': str})
        df.to_csv(download_path, index=False)
    return df

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

def prepare_l_i_requests():
    df = None
    download_path = 'l_i_requests.csv'
    if os.path.exists(download_path):
        print('Cached L&I requests csv found')
    else:
        service_requests_df = get_service_requests()
        violations_df = get_violations()
        l_i_requests_df = service_requests_df.query("agency_responsible == 'License & Inspections'").sample(n=10)
        l_i_requests_df['opa_account_num'] = l_i_requests_df['address'].apply(request_opa_account_number)
        df = pd.merge(violations_df, l_i_requests_df, how='inner', on='opa_account_num')
        df.to_csv(download_path, index=False)

prepare_l_i_requests()
