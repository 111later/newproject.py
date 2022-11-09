import requests
from bs4 import BeautifulSoup

USD_BYN = "https://yandex.by/search/?text=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B1%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC%D1%83&lr=157&search_source=yaby_desktop_common&src=suggest_B"
headers = {"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"}
full_page = requests.get(USD_BYN, headers = headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.find_all("span", {"class": "Textinput ConverterTextinput"})
print(convert[0].text)
