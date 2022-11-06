# import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

data=[]
for page in range(1,51,1):
    url = "https://www.arabam.com/ikinci-el?take=50&page=" + str(page) # url of the website
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(url, headers=headers).text # connect to website
    soup = BeautifulSoup(page,"html.parser") # raw data
    notices = soup.find_all("tr",class_="listing-list-item pr should-hover bg-white") # filtering the data

    for notice in notices:
        item={}
        item["model"]= notice.find("div",class_="listing-text-new word-break val-middle color-black2018").text.strip() # model of the car
        item["price"]= notice.find("span", class_="db no-wrap listing-price").text.strip() # price of the car
        item["year"]= notice.find("td", class_="listing-text").text.strip() # Year(Model) of the car
        item["province"]= notice.find("span", class_="").text.strip() # Province (il)
        item["date"]= notice.find("td", class_="listing-text tac").text.strip() # Date
        data.append(item)

# export data to excel
df = pd.DataFrame(data)
df.to_excel("arabam.xlsx")
df.to_csv("arabam.csv")