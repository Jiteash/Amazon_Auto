from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from xlwt import Workbook
import time
import xlwt

class AmazonWeb():

    def __init__(self, items):
        #Get URL
        self.amazon_url = "https://www.amazon.com/"
        self.items = items
        #Get driver path
        self.driver = webdriver.Chrome()
        self.driver.get(self.amazon_url)


    def search_items(self):
          #Calling excel library
          wb= Workbook()
          Paperback_prices=[]
          Kindle_prices=[]
          Title=[]
          print("searching",items)
          self.driver.get(self.amazon_url)
          #passing the category type
          a = Select(self.driver.find_element_by_id("searchDropdownBox"))
          a.select_by_visible_text(categories)
          time.sleep(2)
          #passing the items needs to be searched
          search_input=self.driver.find_element_by_id("twotabsearchtextbox")
          search_input.send_keys(items)
          time.sleep(2)
          #Search started
          search_button=self.driver.find_element_by_class_name("nav-input")
          search_button.click()

          #View first search page
          x=self.driver.find_element_by_css_selector("#search > div.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.s-right-column.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-result-list.sg-row > div:nth-child(1) > div > div > div > div:nth-child(2) > div.sg-col-4-of-12.sg-col-8-of-16.sg-col-16-of-24.sg-col-12-of-20.sg-col-24-of-32.sg-col.sg-col-28-of-36.sg-col-20-of-28 > div > div:nth-child(1) > div > div > div:nth-child(1) > h5 > a > span")
          x.click()
          #productTitle id is common for all elements
          Product_name = self.driver.find_element_by_id("productTitle").text
          Kindle_price = self.driver.find_element_by_css_selector("#mediaTab_heading_0 > a > span > div:nth-child(2) > span").text
          Paperback_price = self.driver.find_element_by_css_selector("#mediaTab_heading_1 > a > span > div:nth-child(2) > span").text
          #adding all result to a list
          Kindle_prices.append(Kindle_price)
          Title.append(Product_name)
          Paperback_prices.append(Paperback_price)
          #creating a spreadsheet
          sheet1= wb.add_sheet('Sheet1')
          sheet1.write(0,0,"Title")
          sheet1.write(0,1,"Kindle price")
          sheet1.write(0,2,"Paperback price")
          sheet1.write(1,0,Product_name)
          sheet1.write(1,1,Kindle_price)
          sheet1.write(1,2,Paperback_price)
          #output will stored by default in Python folder
          wb.save('output.xls')
          print("Title: ",Product_name)
          print("Kindle price: ",Kindle_price)
          print("Paperback price: ",Paperback_price)
          time.sleep(5)

          return Kindle_prices, Title, Paperback_prices
items = "data catalog"
categories="Books"
amazon_bot= AmazonWeb(items)
amazon_bot.search_items()

















