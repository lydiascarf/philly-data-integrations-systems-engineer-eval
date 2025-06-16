import pandas as pd

download_path = '311_requests.csv'
service_requests_df = pd.read_csv(download_path)
l_and_i_requests_df = service_requests_df.query("agency_responsible == 'License & Inspections'")
print(l_and_i_requests_df)
print('------ hi ------')
print(l_and_i_requests_df.iloc[0,7])
