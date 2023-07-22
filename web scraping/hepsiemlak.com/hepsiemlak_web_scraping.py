# This code meant to scrap data from hepsiemlak around 25000+ notices were scraped and put into excel table.
# Later this data will be analyzed to see housing prices in Turkey by province.

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
data=[]

for page in range(1,1183,1):
    url = "https://www.hepsiemlak.com/kiralik/daire?page=" + str(page) # url of the website
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    time.sleep(1)
    page = requests.get(url, headers=headers).text # connect to website
    soup = BeautifulSoup(page,"html.parser") # raw data
    notices = soup.find_all("div",class_="list-view-content") # filtering the data

    for notice in notices:
        item={}
        item["price"]= notice.find("span",class_="list-view-price").text.strip() # gets the price
        item["room"]= notice.find("span",class_="celly houseRoomCount").text.strip() # gets the room count
        item["metrekare"]= notice.find("span",class_="celly squareMeter list-view-size").text.strip() # gets the squaremeter
        href_value= notice.find("a").get("href")
        start_index = href_value.find('/') + 1
        end_index = href_value.find('-', start_index)
        item["location"]= href_value[start_index:end_index] # province of the house
        data.append(item)

df = pd.DataFrame(data)
df.to_excel("hepsiemlak.xlsx") # save the scraped data to excel file.