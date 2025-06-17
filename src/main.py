import os
import pandas as pd


def find_2025_l_i_requests(df):
    df['requested_datetime'] = pd.to_datetime(df['requested_datetime'])
    return df[df['requested_datetime'].dt.year == 2025]

def find_requests_violation_issued(df):
    return df[df['violationnumber'].notna()]

def find_requests_not_closed(df):
    df['closed_datetime'] = pd.to_datetime(df['closed_datetime'], errors='coerce')
    return df[df['closed_datetime'].isna()]

def run_analysis():
    df = pd.read_csv('l_i_requests.csv')
    output_dir = '/output'
    os.makedirs(output_dir, exist_ok=True)

    current_year_requests = find_2025_l_i_requests(df)
    current_year_requests.to_csv(f'{output_dir}/current_year_requests.csv', index=False)

    requests_violation_issued = find_requests_violation_issued(current_year_requests)
    requests_violation_issued.to_csv(f'{output_dir}/requests_violation_issued.csv', index=False)

    requests_not_closed = find_requests_not_closed(current_year_requests)
    requests_not_closed.to_csv(f'{output_dir}/requests_not_closed.csv', index=False)

    output = (f'Current year L&I requests count: {len(current_year_requests)}\n'
              f'Current year L&I requests percent with violation issued: {len(requests_violation_issued) / len(df) * 100}\n'
              f'Current year L&I requests percent not closed: {len(requests_not_closed) / len(df) * 100}\n'
              )
    print(output)
    with open(os.path.join(output_dir, 'summary.txt'), 'w') as f:
        f.write(output)


run_analysis()

