import os
import pandas as pd

def get_311_requests_csv():
    service_requests_df = None
    download_path = '311_requests.csv'
    if os.path.exists(download_path):
        print('Cached 311 requests csv found')
        service_requests_df = pd.read_csv(download_path)
    else:
        print('Downloading 311 requests csv')
        url = f'https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20FROM%20public_cases_fc%20WHERE%20requested_datetime%20%3E=%20%272025-01-01%27%20AND%20requested_datetime%20%3C%20%272026-01-01%27'
        service_requests_df = pd.read_csv(url)
        service_requests_df.to_csv('311_requests.csv', index=False)
    return service_requests_df

get_311_requests_csv()
