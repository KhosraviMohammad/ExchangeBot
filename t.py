import requests
import json
import time
import datetime
import pickle

print('started')

data = {"IsSymbolCautionAgreement": False, "CautionAgreementSelected": False, "IsSymbolSepahAgreement": False,
        "SepahAgreementSelected": False, "orderCount": 660, "orderPrice": 14370, "FinancialProviderId": 1,
        "minimumQuantity": 0,
        "maxShow": 0, "orderId": 0, "isin": "IRO1PYPD0001", "orderSide": 65, "orderValidity": 74,
        "orderValiditydate": None,
        "shortSellIsEnabled": False, "shortSellIncentivePercent": 0}

header = {'Authorization': "BasicAuthentication b8dd8900-c4df-4700-816e-cd4488b59d8c",
          'Content-Type': 'application/json'}
IsSuccessfull = False
response_list = []
i = 0

order_urls = "https://api3.mobinsb.ir/Web/V1/Order/Post"

status_urls = 'https://core.tadbirrlc.com//StockFutureInfoHandler.ashx?%7B%22Type%22:%22getLightSymbolInfoAndQueue%22,%22la%22:%22Fa%22,%22nscCode%22:%22IRO1PYPD0001%22%7D&jsoncallback='

while True:
    status_response = requests.get(status_urls)
    print(f'status_response:', status_response, '\n')
    status_response_content = json.loads(status_response.content)
    new_price = status_response_content.get('symbolinfo').get('ht')
    if new_price != data.get("orderPrice"):
        data['orderPrice'] = new_price
        break

data_j = json.dumps(data)

# date_time_start = datetime.datetime(2023, 5, 5, 9, 59, 59, 989999)

while not IsSuccessfull:
    response = requests.post(order_urls, data=data_j, headers=header)
    response_list.append(response)
    response_content = json.loads(response.content)
    IsSuccessfull = response_content.get('IsSuccessfull')
    i += 1
    print(f'i{i}: {response_content}', '\n')
    time.sleep(0.1199999)

with open(r'D:\programming\python\python\project\ExchangeBot\response.txt', 'bw') as file:
    pickle.dump(response_list, file)

end = 'end'
