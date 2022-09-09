from asyncore import ExitNow
import selenium
from selenium import webdriver
import requests
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# # driver  = webdriver.Chrome(ChromeDriverManager().install())
# chrome_options = webdriver.ChromeOptions()
# # driver = webdriver.Chrome(options=chrome_options,executable_path='/Downloads/chromedriver')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # sleep(5)

# while(True):
options = Options()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

    
# driver = webdriver.Chrome(options=chrome_options,executable_path='/Downloads/chromedriver')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
 

try:
    driver.get('https://www.walmart.com/browse/patio-garden/fertilizer/5428_4091_6107689_6012089')
    sleep(20) 
except:
    driver.refresh()
    # import pdb

    # pdb.set_trace()    

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)
    # table = soup.findAll('a', attrs = {'class':'absolute w-100 h-100 z-1 hide-sibling-opacity'})
table=soup.findAll('div', attrs = {'class': 'mb1 ph1 pa0-xl bb b--near-white w-25'})


print('table',table)




