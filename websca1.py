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
        self.driver.maximize_window()
        
        
    def search_items(self):
        for item in self.items:
            self.amazon_url = "https://www.amazon.in/"
            self.items = items
            self.driver = webdriver.Firefox(executable_path="C:\\Users\\Asus\\Desktop\\geckodriver.exe")
            self.driver.maximize_window()
            print(f"Searching for {item}.")
            
            driver = self.driver.get(self.amazon_url)
                            
            search_input = self.driver.find_element_by_id("twotabsearchtextbox")
                            
            search_input.send_keys(item)

            
            
            search_button = self.driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
            search_button.click()
            
            search_button = self.driver.find_element_by_link_text(item).click()
            

            chwd = self.driver.window_handles
            
            for w in chwd:
                
                
        
                self.driver.switch_to.window(w)
                    
    
            time.sleep(0.9)
            
            url=self.driver.current_url
            
            headers= ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
            page=requests.get(url=url,headers=headers)
            soup = BeautifulSoup(page.content,'lxml')
            c = soup.find("div",id="detailBulletsWrapper_feature_div").text
            print(c)
            self.driver.quit()
           
            
            items = ["Kaaval Kottam","Kutrap Parambarai"]
amazon_bot = AmazonBot(items)
amazon_bot.search_items()
print("success")
#/html/body/div[2]/div[2]/div[3]/div[1]/div[5]/div[27]/div/div/div/div/div[3]/a/span
