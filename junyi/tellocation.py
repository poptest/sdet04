import requests

url = "http://apis.juhe.cn/mobile/get?phone=13429667914&key=802831374e480e92f88f1bd989a805b0"
resp = requests.get(url)
print(resp.status_code)
print(resp.content)