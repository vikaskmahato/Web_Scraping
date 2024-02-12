import requests
import pandas as pd
from bs4 import BeautifulSoup
from mysql_connector import engine


# find all occurrences of a tag or set of tags that match the specified criteria
def product_name(content_div):
    names = content_div.find_all("div", attrs={'class':'_4rR01T'})
    items = []
    for i in names:
        # print(i.text)
        items.append(i.text)

    # print(len(items))
    return items

def product_price(content_div):
    prices = content_div.find_all("div", attrs={'class':'_30jeq3 _1_WHN1'})
    items_price = []
    for i in prices:
        # print(i.text)
        items_price.append(i.text)

    # print(len(items_price))
    return items_price

def product_description(content_div):
    description = content_div.find_all("ul", attrs={'class':'_1xgFaf'})
    items_desc = []
    for i in description:
        # print(i.text, '--')
        desc_list = i.find_all("li", attrs={'class': 'rgWa7D'})
        list_str = ''
        for j in desc_list:
            list_str = list_str + j.text + '||'
            
        # print(list_str)
        items_desc.append(list_str)  
    # print(len(items_desc))
    return items_desc

def product_rating(content_div):
    rating = content_div.find_all("div", attrs={'class':'_3LWZlK'})
    items_rating = []
    for i in rating:
        # print(i.text, '--')
        items_rating.append(i.text)

    print(len(items_rating))
    return items_rating



headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}) 

for i in range(1,24):
    url = "https://www.flipkart.com" + "/search?q=laptop&amp;otracker=search&amp;otracker1=search&amp;marketplace=FLIPKART&amp;as-show=on&amp;as=off&amp;page=" + str(i)

    page = requests.get(url= url, headers= headers)

    print(page)

    soup = BeautifulSoup(page.content, "html.parser")

    #locate the first occurrence of a tag or a set of tags that match the specified criteria
    content_div = soup.find("div", attrs={'class':'_1YokD2 _3Mn1Gg'})
    # print(soup)
    names = product_name(content_div)
    prices = product_price(content_div)
    description = product_description(content_div)
    rating = product_rating(content_div)
    # print(description)
    products_dict = {'product_name': names, 'product_price': prices, 'product_description': description, 'product_rating': rating}
    df = pd.DataFrame(products_dict)
    print(df.head(10))

    with engine.begin() as conn:
    # Invoke DataFrame method to_sql() to
    # create the table and
    # insert all the DataFrame rows into it
        df.to_sql(
            name='flipkart_data', # database table
            con=conn, # database connection
            index=False # Don't save index
        )
    # df.to_csv(r"C:\Users\vikas\Documents\mydata.csv")
        
# Reading offline csv files
files = {"CPU": r"C:\Users\vikas\Dow\CPU_UserBenchmarks.csv"}
    


    