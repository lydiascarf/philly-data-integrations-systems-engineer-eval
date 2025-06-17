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
    current_year_requests = find_2025_l_i_requests(df)
    current_year_requests.to_csv('current_year_requests.csv', index=False)
    print("current year requests")
    print(len(current_year_requests))

    requests_violation_issued = find_requests_violation_issued(current_year_requests)
    requests_violation_issued.to_csv('requests_violation_issued.csv', index=False)
    print("percent violation issued")
    print(len(requests_violation_issued) / len(df) * 100)

    requests_not_closed = find_requests_not_closed(current_year_requests)
    requests_not_closed.to_csv('requests_not_closed.csv', index=False)
    print("percent not closed")
    print(len(requests_not_closed) / len(df) * 100)

run_analysis()

