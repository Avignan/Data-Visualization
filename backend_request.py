import datetime
import os
import pandas as pd
import requests
from dotenv import find_dotenv, load_dotenv

CHARTS = {
    2020: {
        'Data Scientist': [
            "job_postings",
            "avg_salary",
            "highest_salary",
        ],
        'Data Analyst': [
            "job_postings",
            "avg_salary",
            "highest_salary",
        ],
        'Machine Learning Engineer': [
            "job_postings",
            "avg_salary",
            "highest_salary",
        ],
    },
    2021: {
        'Data Scientist': [
            "job_postings",
            "avg_salary",
            "highest_salary",
        ],
        'Data Analyst': [
            "job_postings",
            "avg_salary",
            "highest_salary",
        ],
        'Machine Learning Engineer': [
            "job_postings",
            "avg_salary",
            "highest_salary",
        ],
    },
    2022: {
        'Data Scientist': [
            "job_postings",
            "avg_salary",
            "highest_salary",
        ],
        'Data Analyst': [
            "job_postings",
            "avg_salary",
            "highest_salary",
        ],
        'Machine Learning Engineer': [
            "job_postings",
            "avg_salary",
            "highest_salary",
        ],
    }
}

dictionary_input = [{'year': 2022, 'job_title': 'Data Scientist', 'job_postings': 179470, 'avg_salary': 7042285, 'highest_salary': 80031}]

def make_charts(input):
    dct = {k: [v] for k, v in input[0].items()}
    year = [value for key, value in dct.items() if key == 'year'][0][0]
    df = pd.DataFrame(dct)
    all_df = []
    for charts, all_columns in CHARTS[int(year)].items():
        columns = all_columns.copy()
        # total_column = all_columns[-1]
        temp_df = df[all_columns].copy()
        temp_dict = {
            "dataframe": temp_df,
            "column_names": columns.copy(),
            "column_values": [dct[column][0] for column in columns],
        }
        all_df.append(temp_dict.copy())

    return all_df

