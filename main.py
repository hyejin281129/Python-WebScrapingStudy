import requests as rq
from bs4 import BeautifulSoup

# 받아오기
html = rq.get("http://land.sgkyocharo.com/search?q=원룸&type=offer")
print(html)

# parser
parser = BeautifulSoup(html.content, "lxml")
address = parser.find_all(class_ = "address")
priceview = parser.find_all(class_ = "priceview")

addressList = []
preceviewList = []

# address
for a in address:
  addressList.append(a.text)

# preceview
for p in priceview:
  preceviewList.append(p.text)


for i in range(len(preceviewList)):
  print(addressList[i] + '  '+ preceviewList[i])

