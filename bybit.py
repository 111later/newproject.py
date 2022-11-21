import time

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_order():
    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"
    }
    url = "https://www.bybit.com/trade/usdt/BTCUSDT"
    r = requests.get(url=url, headers = headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_orders = soup.find_all("div", {"class" : "ob__table-record "})
    clear_ank = []
    for i in articles_orders:
        articles_title = i.find("div", {"class" : "ob__table-qty ob-highlight--dec"}).text.strip()
        articles_desc_sell =i.find("div", {"class" : "ob__table-record ob__table-sell"}).text.strip()

        articles_time = i.find("time").get("datetime")
        date_from_iso = datetime.fromisoformat(articles_time)
        date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
        articles_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())
        clear_ank.append(i.getText())

        print(f"{articles_title} | {articles_date_timestamp} | {articles_desc_sell}")
        print(len(clear_ank))
        print(clear_ank)

def main():
    print(get_order())
if __name__ == "__main__":
    main()

