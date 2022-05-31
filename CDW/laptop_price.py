from bs4 import BeautifulSoup
import requests


def cdw_prices():
     url = "https://www.cdwg.com/product/hp-zbook-firefly-14-g8-mobile-workstation-14-core-i5-1135g7-16-gb-ra/6421472"
     result = requests.get(url)
     site_html = BeautifulSoup(result.text, "html.parser")
     laptop_price = site_html.find("span", class_="price-type-selected")
     laptop_name = site_html.find("span", class_="mfeo-list-name")
     current_laptop_price = {
          "Price" : laptop_price.string,
          "Name" : laptop_name.string
     }
     return current_laptop_price



#cdw usees cookies/login info to display the Ensign price. need to figure out a way to always display the
#Ensign price. Current price shown is the advertised price w/o Ensign discount.

## TODO: Get the laptop name and return the name and price in a dictionary
