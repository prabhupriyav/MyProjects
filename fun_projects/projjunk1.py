import requests

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
         # print(j)
              asst_exchange = j['exchange_id']
              asst_name = j['base_asset']
              asst_price = j['price']
              asst_vol_24h = j['volume_24h']
              asst_symbol = j['symbol']
              asst_change_24h = j['change_24h']

              asst_list.append([asst_exchange,asst_symbol,asst_name,asst_price,asst_vol_24h,asst_change_24h])
print(asst_list)
