import os
import pandas as pd

def get_311_requests_csv():
    df = None
    download_path = '311_requests.csv'
    if os.path.exists(download_path):
        print('Cached 311 requests csv found')
        service_requests_df = pd.read_csv(download_path)
    else:
        print('Downloading 311 requests csv')
        url = "https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20FROM%20public_cases_fc%20WHERE%20requested_datetime%20%3E=%20%272025-01-01%27%20AND%20requested_datetime%20%3C%20%272026-01-01%27"
        df = pd.read_csv(url)
        df.to_csv(download_path, index=False)

def get_violations_csv():
    df = None
    download_path = 'violations.csv'
    if os.path.exists(download_path):
        print('Cached violations csv found')
        df = pd.read_csv(download_path)
    else:
        print('Downloading violations csv')
        url = "https://phl.carto.com/api/v2/sql?&filename=violations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20violations%20WHERE%20violationdate%20%3E=%20%272019-01-01%27"
        df = pd.read_csv(url)
        df.to_csv(download_path, index=False)

get_311_requests_csv()
get_violations_csv()
