import requests
from bs4 import BeautifulSoup
import json

mystocks = ['TVE.TO', 'BNS.TO', 'BMO.TO', 'RY.TO']
stockdata = []


def getData(symbol):
    headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    url = f'https://ca.finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
    'symbol' : symbol,
    'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    # 'summary': soup.find('div', {'class': 'businessSummary Mt(10px) Ov(h) Tov(e)'}).find_all('p')[1].text,
    }
    return stock

for item in mystocks:
    stockdata.append(getData(item))
    print("Getting:", item)

with open('Stockdata.json', 'w') as f:
    json.dump(stockdata, f)


print('fin .')






# price = soup.find('fin-streamer', {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
# change = soup.find('fin-streamer', {'class': "Fw(500)"}).text
# print(price)


# print (price,change)