import json
import requests
import csv

URL = "https://fapi.binance.com/fapi/v1/exchangeInfo";

response = requests.get(URL)
responseJson = response.json()

symbols = responseJson["symbols"]

file=open("symbol.csv","w",newline="")

writer=csv.writer(file)

header=("Symbol","Base Asset","Quote Asset")
writer.writerow(header)

for i in symbols:
    row=(i["symbol"],i["baseAsset"],i["quoteAsset"])
    writer.writerow(row)
    


file.close()

