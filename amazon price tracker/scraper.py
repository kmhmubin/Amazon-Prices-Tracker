# import packages
import re
import requests
from bs4 import BeautifulSoup

# amazon product url link
url = "https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=sr_1_1?fst=as%3Aoff&qid=1578819515&rnid=16225007011&s=computers-intl-ship&sr=1-1"


# Price converter
def converted_price(price):
    convert_price = float(re.sub(r"[^\d.]", "", price))  # converting the string into float
    return convert_price


# Scarping product details
def products_details():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}

    details = {"name": "",
               "price": 0,
               "deal": True,
               "url": ""}
    _url = url  # calling the url link
    if _url == "":  # checking the url is empty or not
        details = None  # if url empty it will print None
    else:  # if the url not empty
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")  # it will find the product title
        price = soup.find(id="priceblock_dealprice")  # it will find the deal price
        if price is None:  # if there is no deal price
            price = soup.find(id="priceblock_ourprice")  # it will check amazon price
            details["deal"] = False  # if there is no deal price it will print false
        if title is not None and price is not None:  # if the title and price is valid
            details["name"] = title.get_text().strip()  # it will extract the title name and print
            details["price"] = converted_price(
                price.get_text())  # calling the convert price function and print the price
            details["url"] = _url  # print the url
        else:
            return None  # if nothing found it will print None
    return details


# run the function and print the details
print(products_details())
