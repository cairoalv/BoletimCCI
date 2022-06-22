from lib2to3.pgen2 import token
from urllib import response
from wsgiref import headers
import requests
import json


infor = {
    "usuario": "setape",
    "senha": "setape"
  }

url = requests.post("https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Autenticacao", json=infor)
print(url.text)

token = url.text

with open ('token.txt', 'w') as file:
    file.write(token)
