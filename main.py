import requests
from bs4 import BeautifulSoup
from decouple import config
from bot import FormsSheetsBot

URL = config("URL")
FORMS_URL = config("FORMS_URL")
USER_AGENT = config("USER_AGENT")
LANGUAGES = config("ACCEPT_LANGUAGE")

http_headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": LANGUAGES
}

bot = FormsSheetsBot()

response = requests.get(URL, headers=http_headers).text
soup = BeautifulSoup(response, "html.parser")

addresses = soup.find_all("address", class_="list-card-addr")
prices = soup.find_all("div", class_="list-card-price")
links = soup.find_all("a", class_="list-card-link")

address_list = [address.getText() for address in addresses]
price_list = [price.getText().split(" ")[0] for price in prices]
link_list = [link.get("href") for link in links]

bot.submit_forms(FORMS_URL, address_list, price_list, link_list)
