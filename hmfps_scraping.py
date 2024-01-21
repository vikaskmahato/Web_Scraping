import re
from selenium.webdriver.common.by import By

# input_string = "{id:'https://www.userbenchmark.com/EFps/,2070S,,_,2080,,_Fortnite,,9400F,',t:'Nvidia 2070S',p:'163'}"

# # Define a function to add quotes around keys and values
# def add_quotes(test):
#     print(test)
#     key = test.group(1)
#     print(key)
#     value = test.group(2)
#     print(value)
#     return f"'{key}': '{value}'"

# # Use regular expressions to find and modify key-value pairs
# output_string = re.sub(r'(\w+):([^,}]+)', add_quotes, input_string)

# print(output_string)

from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re
import json




headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}) 

url = "https://howmanyfps.com/laptops"

page = requests.get(url= url, headers= headers)

print(page)

soup = BeautifulSoup(page.content, "html.parser")

dropdown = soup.find_all('article', attrs= {'class': 'ra'})
# print(dropdown)
for i in dropdown:
    print(i.text, '--')

# input_element = soup.find('input', {'id': 'i33-input'})
# print(input_element)
# Print the value attribute of the input element
# if input_element:
#     placeholder_value = input_element.get('placeholder')
#     print(f"Placeholder Value: {placeholder_value}")
# else:
#     print("Input element not found.")
      

# driver = webdriver.Chrome()  # or use webdriver.Firefox()

# try:
#     driver.get(url)

#     # Assuming you have some code to interact with the dropdown, for example:
#     dropdown = driver.find_element(By.ID, 'i33-input')
#     dropdown.send_keys('Horizon Zero Dawn')  # Replace 'Your Dropdown Value' with the actual value you want to select

#     # Wait for the page to load (you may need to adjust the time based on your page)
#     driver.implicitly_wait(5)

#     # Get the HTML content of the page after selecting a dropdown value
#     page_source = driver.page_source

#     # Parse the HTML content with BeautifulSoup
#     soup = BeautifulSoup(page_source, 'html.parser')

#     # Extract and process the data you need from the soup object
#     # ...
#     print(soup)
# finally:
#     # Close the webdriver
#     driver.quit()