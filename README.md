# web-scraping-project
In this project, I built a script to scrape the website Flipkart for cell phone product data.

First I downloaded the libraries requests and BeautifulSoup. The requests library allows you to make HTTP requests, so that  you can request for a website to send you its HTML code. The BeautifulSoup library allows you to parse the HTML data you receive.

After importing these libraries, I requested the URL of the first page that I wanted to scrape (ie the first page of cellphone product data). I then created a for loop to iterate through each webpage. Within the loop, I created a request object and a BeautifulSoup object as well as a list to store all of the cellphone product HTML data. I also created another inner for loop to iterate through each product on the page. Within this inner loop, I an object for the product name, price and rating, then converted these objects to strings and printed them out. Lastly, in the outer loop I assigned the next webpage to the URL in order to iterate to the next page.

This project is intended to demonstrate one of the first steps of the data analysis process.
