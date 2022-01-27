import requests
import csv
import datetime
from tabulate import tabulate
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
## Function api_calls - fetches data from the API

def api_calls():

    ## Get the exchanges data
    url = "https://www.cryptingup.com/api/exchanges"
    exchg = requests.get(url)
    exchg_list = dict(exchg.json())
    exchg_ig = exchg_list['exchanges']
    exchg_final_list = []
    asst_list = []
    for i in exchg_ig:
    ## Get the Market data with exchane id
        url = "https://www.cryptingup.com/api/exchanges/{}/markets".format(i['id'])
        mrkt = requests.get(url)
        mrkt_list = dict(mrkt.json())
        mrkt_ig = mrkt_list['markets']

        for j in mrkt_ig:
            asst_exchange = j['exchange_id']
            asst_name = j['base_asset']
            asst_price = j['price']
            asst_vol_24h = j['volume_24h']
            asst_list.append([asst_exchange,asst_name,asst_price,asst_vol_24h])

    fields = ['Exchg', 'asset', 'price', 'vol24']
#filename = "./exch_asset"+str(datetime.datetime.now())+'.csv'
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(asst_list)
        csvfile.close()

        #print(tabulate(asst_list,headers = ["Exchange Id","Asset","Price","24H Volume"]))
def plot_values():
    #print(filename)
    #print(os.getcwd())
    stock_df = pd.read_csv(filename)
    stock_val = stock_df.sort_values(by = 'price', ascending = False)[:10]
    #print(stock[stock['Exchg'].isin([''])])
    plt.figure(figsize = (15,5))
    print(plt.bar(stock_val['Exchg'], stock_val['price']))
#    print(stock)


filename = "./exch_asset"+(str(datetime.datetime.now()).replace(" ",""))+'.csv'
api_calls()
plot_values()
