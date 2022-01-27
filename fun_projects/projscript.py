import requests
import csv
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class crypto_exchg:
    def __init__(self):
        self.exchanges = []
        self.vol24 = []
        self.assets = []
        self.filename = "./exch_asset"+(str(datetime.datetime.now()).replace(" ",""))+'.csv'

    def api_calls(self):

        ## Get the exchanges data
        url = "https://www.cryptingup.com/api/exchanges"
        exchg = requests.get(url)
        exchg_list = dict(exchg.json())
        exchg_ig = exchg_list['exchanges']
        exchg_final_list = []
        asst_list = []
        for i in exchg_ig:
            self.exchanges.append(i['id'])
            self.vol24.append(i['volume_24h'])
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
                asst_symbol = j['symbol']
                asst_change_24h = j['change_24h']
                asst_list.append([asst_exchange,asst_symbol,asst_name,asst_price,asst_vol_24h,asst_change_24h])

        fields = ['Exchg','symbol','asset','price','vol24','change24']
        with open(self.filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(asst_list)
            csvfile.close()

    def plot_values(self):

        stock_df = pd.read_csv(self.filename)
        print(" TOP ASSETS BASED ON PRICE ACROSS ALL EXCHANGES")
        stock_val = stock_df.sort_values(by = 'price', ascending = False)[:30]
        display(stock_val)
        print(" \n")
        print("AVERAGE PRICE OF ASSETS IN EACH EXCHANGE")
        avrg_price = stock_df.groupby(by = 'Exchg')['price'].mean()
        display(avrg_price)
        print(" \n")

        for exchg in self.exchanges:
            print(f'TOP 5 ASSETS OF {exchg} BY PRICE')
            coin_df = stock_df[stock_df['Exchg'].isin([exchg])]
            sort_coin = coin_df.sort_values(by = 'price', ascending = False)[:5]
            display(sort_coin)
            print(f'TOP 5 ASSETS OF {exchg} BY 24H VOLUME')
            sort_coin1 = coin_df.sort_values(by = 'vol24', ascending = False)[:5]
            display(sort_coin1)
            print(" \n")


        plt.figure(figsize=(16,19))

        ax1 = plt.subplot(2,1,1)
        ax1.set_title("Volume change in 24H of Exchanges")
        ax1.plot(stock_df['Exchg'],stock_df['vol24'])


        ax2 = plt.subplot(2,1,2)
        ax2.set_title("Price Range vs Exchanges")
        ax2.bar(stock_df['Exchg'],stock_df['price'],color = 'orange')

my_crypto = crypto_exchg()
my_crypto.api_calls()
my_crypto.plot_values()
