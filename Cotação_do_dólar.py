import requests
req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(req)
print(req.json())
Js = req.json()
print(Js['USDBRL']['bid'])
