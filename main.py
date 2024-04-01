# import asyncio
# import grequests
import requests
import json
import time
import datetime
import pickle
import pause

data = {"IsSymbolCautionAgreement": False, "CautionAgreementSelected": False, "IsSymbolSepahAgreement": False,
        "SepahAgreementSelected": False, "orderCount": 4996, "orderPrice": 1994, "FinancialProviderId": 1,
        "minimumQuantity": 0,
        "maxShow": 0, "orderId": 0, "isin": "IRO7CMIZ0001", "orderSide": 65, "orderValidity": 74,
        "orderValiditydate": None,
        "shortSellIsEnabled": False, "shortSellIncentivePercent": 0}

header = {'Authorization': "BasicAuthentication 4b06e183-9195-4093-b443-a231728905eb",
                               'Content-Type': 'application/json'}
data_j = json.dumps(data)

urls = "https://api3.mobinsb.ir/Web/V1/Order/Post"

urls_status = 'https://core.tadbirrlc.com//StockFutureInfoHandler.ashx?%7B%22Type%22:%22getLightSymbolInfoAndQueue%22,%22la%22:%22Fa%22,%22nscCode%22:%22IRO1PYPD0001%22%7D&jsoncallback='

date_time_start = datetime.datetime(2023, 5, 13, 8, 44, 59, 989999)
IsSuccessfull = False
response_list = []
i = 0
print('started')

while not IsSuccessfull:
    if datetime.datetime.now() >= date_time_start:
        response = requests.post(urls, data=data_j, headers=header)
        response_list.append(response)
        response_content = json.loads(response.content)
        IsSuccessfull = response_content.get('IsSuccessfull')
        i += 1
        print(f'i: {response_content}', '\n')
        time.sleep(0.1199999)


with open(r'D:\programming\python\python\project\ExchangeBot\response.txt', 'bw') as file:
    pickle.dump(response_list, file)

end = 'end'
