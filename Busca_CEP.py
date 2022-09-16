import requests
req = requests.get("https://cep.awesomeapi.com.br/json/90630160")
print(req)
print(req.json())
Js = req.json()
print(Js['cep']),print(Js['address']),print(Js['district']),print(Js['city']),print(Js['city_ibge'])
