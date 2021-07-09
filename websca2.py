import csv
from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import time
rows=[] 
class AmazonBot(object):
    def __init__(self,items):
        self.amazon_url = "https://www.amazon.in/"
        self.items = items
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Asus\\Desktop\\geckodriver.exe")
        self.driver.maximize_window()
        
        
    def search_items(self):
        global rows
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
            
            l=(c.split("\n"))
            k=[]
            for i in l:
                if i != "":
                    k.append(i)
            k.pop(0)

            z=0
            for i in k:
                z+=1
                if i == ":":
                    k.pop(z)
                    k.pop(z-2)
                    k.remove(i)
            z=0
            fields=[]
            row=[]
            for j in k:
                if z%2==0:
                    fields.append(j)
                else:
                    row.append(j)
                z+=1
            rows.append(row)
            self.driver.quit()
        
        return fields,rows
        
    
items = ["Kaaval Kottam","Kutrap Parambarai"]
amazon_bot = AmazonBot(items)
(fields,rows) = amazon_bot.search_items()
t=(fields,rows)
f1=list(t[0])
r=list(t[1])
with open('GFG.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(items) 
    write.writerow(r)   
print("success")      


    




