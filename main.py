import requests
import os
import configparser

from datetime import datetime, timedelta
import pandas as pd
import pandas_datareader.data as reader
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np


#API Key
config = configparser.ConfigParser()
config.read("config.ini")
T_API_Key = config["DEFAULT"]["TIINGO_API_KEY"]

### Getting Data ###
def get_last_200_days_prices(ticker, api_key):
    #Define Request Information
    headers = {
        "Content-Type" : "application/json",
        "Authorization" : f"Token {api_key}"
    }

    start_date = datetime.now().date() - timedelta(days=240)
    end_date = datetime.now().date()

    formatted_start_date = f"{start_date.year}-{start_date.month}-{start_date.day}"
    formatted_end_date = f"{end_date.year}-{end_date.month}-{end_date.day}"
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate={start_date}&endDate={end_date}"

    ### Need to add cache ###

    #Request
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return 
    
    data = response.json()
    if not data:
        print("Error getting JSON Data")
        return
    
    ### Need to add data to prices [] ###

    prices = []
    print(data)
    # for element in data:
    #     prices.insert(0, data["adjClose"])
    return prices


#Fake Asset
test_money = 100000
assets_held = 0

### Basic Moving Average Crossover ###
short_window = 30
long_window = 120
#Sample single stock, want to grow this into a matrix of a diversified set of assets for more complicated strategies
data = get_last_200_days_prices("RIVN", T_API_Key)
print(data)





