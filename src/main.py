import pandas as pd


def run_analysis():
    df = pd.read_csv('l_i_requests.csv')
    print(df)

run_analysis()

