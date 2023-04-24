import requests
from bs4 import BeautifulSoup
import json

import requests
from bs4 import BeautifulSoup
import json

symbol = input("Enter a stock symbol: ")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
url = f'https://ca.finance.yahoo.com/quote/{symbol}'
r = requests.get(url, headers=headers)

if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'symbol': symbol,
        'price': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    }
    with open('Stockdata.json', 'w') as f:
        json.dump([stock], f)
    print(f'Successfully scraped data for {symbol} and saved it to Stockdata.json')
else:
    print(f"Failed to get data for {symbol}. Please check the symbol and try again.")







# price = soup.find('fin-streamer', {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
# change = soup.find('fin-streamer', {'class': "Fw(500)"}).text
# print(price)


# print (price,change)