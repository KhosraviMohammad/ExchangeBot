# import asyncio
# import grequests
import requests
import json
import time
import datetime
import pickle
import pause

data = {"IsSymbolCautionAgreement": False, "CautionAgreementSelected": False, "IsSymbolSepahAgreement": False,
        "SepahAgreementSelected": False, "orderCount": 404, "orderPrice": 24650, "FinancialProviderId": 1,
        "minimumQuantity": 0,
        "maxShow": 0, "orderId": 0, "isin": "IRO3FAHZ0001", "orderSide": 65, "orderValidity": 74,
        "orderValiditydate": None,
        "shortSellIsEnabled": False, "shortSellIncentivePercent": 0}

header = {'Authorization': "BasicAuthentication 76d53956-c1d8-4726-b383-7f206eb91220",
                               'Content-Type': 'application/json'}
data_j = json.dumps(data)

urls = "https://api3.mobinsb.ir/Web/V1/Order/Post"

urls_status = 'https://core.tadbirrlc.com//StockFutureInfoHandler.ashx?%7B%22Type%22:%22getLightSymbolInfoAndQueue%22,%22la%22:%22Fa%22,%22nscCode%22:%22IRO1PYPD0001%22%7D&jsoncallback='

date_time_start = datetime.datetime(2023, 6, 12, 8, 44, 59, 989999)
IsSuccessfull = False
response_list = []
i = 0
print('started1')
pause.until(date_time_start)
print('started2')
while True:
    response = requests.post(urls, data=data_j, headers=header)
    response_list.append(response)
    response_content = json.loads(response.content)
    i += 1
    print(f'i: {response_content}', '\n')
    time.sleep(0.12)
    if i >= 20:
        break


with open(r'D:\programming\python\python\project\ExchangeBot\response.txt', 'bw') as file:
    pickle.dump(response_list, file)

end = 'end'
