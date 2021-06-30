from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import time

class AmazonBot(object):
    def __init__(self,items):
        self.amazon_url = "https://www.amazon.in/"
        self.items = items
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Asus\\Desktop\\geckodriver.exe")
        self.driver.get(self.amazon_url)
    def search_items(self):
        for item in self.items:
            print(f"Searching for {item}.")
            
            self.driver.get(self.amazon_url)
                            
            search_input = self.driver.find_element_by_id("twotabsearchtextbox")
                            
            search_input.send_keys(item)

            time.sleep(2)
            
            search_button = self.driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
            search_button.click()
            time.sleep(2)
items = ["kaaval kottam"]
amazon_bot = AmazonBot(items)
amazon_bot.search_items()
print("success")
                            
