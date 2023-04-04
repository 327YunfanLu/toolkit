""" yf_example3.py

Example of download Qantas stock prices for a given year into data folder.
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """
    Download Qantas stock prices for a give year into a CSV file
    """
    start_date= f'{year}-01-01'
    end_date= f'{year}-12-31'
    ticker='QAN.AX'
    output_file=f'qan_prc_{year}.csv'
    output_path=os.path.join(cfg.DATADIR,output_file)
    yf_example2.yf_prc_to_csv(ticker, output_path, start_date, end_date)

if __name__ == "__main__":
    qan_prc_to_csv(year=2021)



