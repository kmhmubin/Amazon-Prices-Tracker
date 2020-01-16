# import packages
import re  # a build-in regular expresion module
import requests
from bs4 import BeautifulSoup

# Storing the link in a variable
URL = "https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=sr_1_1?fst=as%3Aoff&qid=1578819515&rnid=16225007011&s=computers-intl-ship&sr=1-1"


# price converter function
def converted_price(price):
    # convert html elements into float
    convert_price = float(re.sub(r"[^\d.]", "", price))
    return convert_price


# Extract product details function
def product_details():
    # add user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}

    # storing product details in a dictionary
    details = {
        "Name": "",
        "Price": 0,
        "Deal": True,
        "Availability": "",
        "Product URL": ""
    }

    # Calling the url variable
    _url = URL
    # checking the url is empty or not
    if _url == "":
        # if url empty it will print none
        details = None
    # if url not empty
    else:
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        # it will find the product title
        title = soup.find(id="productTitle")
        # it will find the deal price
        price = soup.find(id="priceblock_dealprice")
        # it will check the product is available or not
        stock = soup.find(id="availability")
        # it will check the product is available or not
        if price is None:
            # if there is no deal price
            # it will check amazon price
            price = soup.find(id="priceblock_ourprice")
            details["Deal"] = False  # if no deal it will print False

        # if the title and price is valid
        if title is not None and price is not None:
            # it will extract the title name and print
            details["Name"] = title.get_text().strip()
            details["Price"] = converted_price(
                price.get_text())  # calling the convert price function and print the price
            # it will find the availability of the product and print
            details["Availability"] = stock.get_text().strip()
            details["Product URL"] = _url  # print the product url
        # if nothing found it will print None
        else:
            return None

    return details


# run the function and print the details
print(product_details())
