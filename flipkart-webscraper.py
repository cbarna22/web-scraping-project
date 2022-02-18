#Python Web Scraping Project
#This script scrapes the website Flipkart for cell phone product data.
#The data includes product names, prices, and ratings.
#Libraries used: requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup


#URL of first page to be webscraped
URL = "https://www.flipkart.com/search?q=cell%20phone&otracker="\ 
"search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


for page_iterator in range(10): #for loop iterates through first 10 pages of website
    
    page = requests.get(URL)    #creating requests object

    soup = BeautifulSoup(page.content, "html.parser")   #creating BeautifulSoup object
    
    products = soup.find_all("div", class_="_2kHMtA")   #creating products list (includes
                                                        #html data for product name, price and rating)


    for product in products:                                    #for loop iterates through each product
        product_name = product.find("div", class_="_4rR01T")    #finds name of product in html data
        price = product.find("div", class_="_30jeq3 _1_WHN1")   #finds price of product
        rating = product.find("div", class_="_3LWZlK")          #finds customer rating out of five stars
        
        print("Product name: " + product_name.text)             #printing product data 
        print("Price (INR): " + price.text[1:])                 
        print("Rating: " + rating.text)
        print("\n")

    URL = "https://www.flipkart.com/search?q=cell%20phone&otracker="\   #assigning next page to URL 
    "search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"\
    "&page=" + str(page_iterator)
    
    




            
