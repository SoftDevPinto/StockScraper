import json
import tkinter as tk
import requests
from bs4 import BeautifulSoup

def scrape_stock_data():
    symbol = entry.get()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    url = f'https://ca.finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
        change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
        status_label.config(text=f'Stock symbol: {symbol}\nPrice: {price}\nChange: {change}')
    else:
        status_label.config(text=f"Failed to get data for {symbol}. Please check the symbol and try again.")

root = tk.Tk()
root.title("Stock Data Scraper")

label = tk.Label(root, text="Enter a stock symbol:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Scrape Data", command=scrape_stock_data)
button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()








# price = soup.find('fin-streamer', {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
# change = soup.find('fin-streamer', {'class': "Fw(500)"}).text
# print(price)


# print (price,change)