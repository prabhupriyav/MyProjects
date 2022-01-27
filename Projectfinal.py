import requests
import csv
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Crypto_exchg:
    def __init__(self):
        self.exchanges = []
        self.vol24 = []
        self.assets = []
        self.filename = "./exch_asset"+(str(datetime.datetime.now()).replace(" ",""))+'.csv'
        self.filename_ast = "./asset_det"+(str(datetime.datetime.now()).replace(" ",""))+'.csv'

    def exchange_market(self):

        ## Get the exchanges data
        url = "https://www.cryptingup.com/api/exchanges"
        exchg = requests.get(url)
        exchg_list = dict(exchg.json())
        exchg_ig = exchg_list['exchanges']
        exchg_final_list = []
        asst_list = []
        
        for ex_val in exchg_ig:
            self.exchanges.append(ex_val['id'])
        ## Get the Market data with exchane id
            url = "https://www.cryptingup.com/api/exchanges/{}/markets".format(ex_val['id'])
            mrkt = requests.get(url)
            mrkt_list = dict(mrkt.json())
            mrkt_ig = mrkt_list['markets']

            for ex_as_val in mrkt_ig:
                asst_exchange = ex_as_val['exchange_id']
                asst_name = ex_as_val['base_asset']
                asst_price = ex_as_val['price']
                asst_vol_24h = ex_as_val['volume_24h']
                asst_symbol = ex_as_val['symbol']
                asst_change_24h = ex_as_val['change_24h']
                asst_list.append([asst_exchange,asst_symbol,asst_name,asst_price,asst_vol_24h,asst_change_24h])
        fields = ['Exchg','symbol','asset','price','vol24','change24']
        with open(self.filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(asst_list)
            csvfile.close()
                
    def asset_details(self):

        url = "https://www.cryptingup.com/api/assets"
        asset_det = requests.get(url)
        asset_det_list = dict(asset_det.json())
        asset_det_ig = asset_det_list['assets']
        assetdet_final_list = []
        asstdet_list = []
        for as_det_val in asset_det_ig:
            self.assets.append(as_det_val['id'])

        
    ##Get the asset details for asset
            url = "https://www.cryptingup.com/api/assets/{}".format(as_det_val['id'])
            as_det = requests.get(url)
            as_det_list = dict(as_det.json())
            as_det_ig = as_det_list['asset']
            asst_det_id = as_det_ig['id']
            asst_det_name = as_det_ig['name']
            asst_det_price = as_det_ig['price']
            asst_det_v24h = as_det_ig['volume_24h']
            asst_det_ch1h = as_det_ig['change_1h']
            asst_det_ch24h = as_det_ig['change_24h']
            asst_det_ch7d = as_det_ig['change_7d']
            asst_det_time = as_det_ig['time']
            asstdet_list.append([asst_det_id,asst_det_name,asst_det_price,asst_det_v24h,asst_det_ch1h,asst_det_ch24h,\
                             asst_det_ch7d,asst_det_time])

        fields = ['astid','name','price','vol24','chg1h','chg24h','chg7d','time']
        with open(self.filename_ast, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(asstdet_list)
            csvfile.close()

    def plot_values(self):

        stock_df = pd.read_csv(self.filename)
        asset_df = pd.read_csv(self.filename_ast)
        columns = asset_df[['astid','name','price','time']]
        ### Displays details of the given asset
        inp_asst = (input(" Select an asset to view current price [BTC,ETH,SOL,DOGE,GALA,XLM,ATOM,CLV] : ")).upper()
        asset_spec = asset_df[asset_df['astid'] == inp_asst]
        display(asset_spec)
        
        # Analysis on Exchange Market
        print(" TOP ASSETS BASED ON PRICE ACROSS ALL EXCHANGES")
        stock_val = stock_df.sort_values(by = 'price', ascending = False)[:10]
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
      
        ## Plotting
        
        plt.figure(figsize=(15,5))
        plt.plot(stock_df['Exchg'],stock_df['vol24'])
        plt.title("Volume change in 24H of Exchanges")
        plt.xlabel('Exchanges')
        plt.ylabel('Volume change in 24h');
        
        plt.figure(figsize=(25,15))
        plt.plot(asset_df['astid'],asset_df['chg7d'])
        plt.title("Assets changes in 7 days")
        plt.xticks(rotation=90)
        plt.xlabel('Assets')
        plt.ylabel('change in 7 Days');
        
        plt.figure(figsize=(25,15))
        plt.bar(asset_df['astid'],asset_df['chg24h'])
        plt.xticks(rotation=90)
        plt.title("Assets changes in 24 hours")
        plt.xlabel('Assets')
        plt.ylabel('change in 24 hours');
        
    
my_crypto = Crypto_exchg()
my_crypto.exchange_market()
my_crypto.asset_details()
my_crypto.plot_values()
