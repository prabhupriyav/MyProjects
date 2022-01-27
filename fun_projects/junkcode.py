#if (j['exchange_id'] == i['id']):
      #print(j)
      #    mrkt_exchg_id = i['id']
      #    mrkt_base_asset.append(j['base_asset'])
#        print(f'{mrkt_exchg_id} {mrkt_base_asset}')
  # for k in mrkt_base_asset:
  #url = "https://www.cryptingup.com/api/assets"
#    asst = requests.get(url)
#    asst_list = dict(asst.json())
#    asst_ig = asst_list['assets']
#    asst_final_list = []
#    for a in mrkt_base_asset:
#        for k in asst_ig:
#            if a == k['id']:
#                print(f'{a} {(k["volume_24h"])}')

          #        print(k)
#
## Get the asset data
import requests
url = "https://www.cryptingup.com/api/assets"
asset_det = requests.get(url)
asset_det_list = dict(asset_det.json())
asset_det_ig = asset_det_list['assets']
assetdet_final_list = []
asstdet_list = []
#print(asset_det_ig)
for as_det_val in asset_det_ig:
    assetdet_final_list.append(as_det_val['id'])


##Get the specific asset details for asset
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
    asstdet_list.append([asst_det_id,asst_det_name,asst_det_price,asst_det_v24h,asst_det_ch1h,asst_det_ch24h,\
                     asst_det_ch7d])
print((asstdet_list))
