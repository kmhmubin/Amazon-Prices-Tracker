# import packages

import requests
from bs4 import BeautifulSoup


# URL verification function
def url_verifier(url):
    if url.find("www.amazon.com") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://wwww.amazon.com" + url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.com" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url


# Price converter
def converted_price(price):
    stripped_price = price.strip("$ ,")
    replaced_price = stripped_price.replace(",", "")
    find_dot = replaced_price.find(".")
    to_convert_price = replaced_price[0:find_dot]
    convert_price = int(to_convert_price)

    return convert_price


# Scarping product details
def products_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}

    details = {"name": "", "price": 0, "deal": True, "url": ""}
    _url = url_verifier(url)
    if _url == "":
        details = None
    else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")
        price = soup.find(id="priceblock_dealprice")
        if price is None:
            price = soup.find(id="priceblock_ourprice")
            details["deal"] = False
        if title is not None and price is not None:
            details["name"] = title.get_text().strip()
            details["price"] = converted_price(price.get_text())
            details["url"] = _url
        else:
            return None
    return details


# printing the product details
print(products_details(
    "https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=sr_1_1?fst=as%3Aoff&qid=1578819515&rnid=16225007011&s=computers-intl-ship&sr=1-1"))
