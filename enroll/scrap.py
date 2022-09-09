from logging import exception
from xml.sax.xmlreader import AttributesImpl
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from views import datainsert
# from time import sleep
from random import randint

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
})

description = []
price=[]
title=[]
prod_link=[]


pages = np.arange(1,5)
# print("%%%%%")
try:
    # for page in pages:
        # import pdb

        # pdb.set_trace()
    while 1>0:
        page = requests.get("https://www.walmart.com/browse/patio-garden/fertilizer/5428_4091_6107689_6012089?page="+str(1)+"&affinityOverride=default",headers=HEADERS)

        # print('$$$$',page.content)

        print("@@@")
        soup = BeautifulSoup(page.text, 'html.parser')
        # print("^^^",soup)
        parent_div = soup.findAll('div', attrs = {'class': 'mb1 ph1 pa0-xl bb b--near-white w-25'})
        # print(parent_div)

        # sleep(5)
        # print(parent_div)
        print('&&&&')
        
        
        for one_div in parent_div:

            link = one_div.find('a',attrs = {'class':'absolute w-100 h-100 z-1 hide-sibling-opacity'})

            print(link)
           

            title= one_div.find('span',attrs = {'class':'f6 f5-l normal dark-gray mb0 mt1 lh-title'}).text

            print(title)
            
            try:
                price = one_div.find('div',attrs = {'class':'b black f5 mr1 mr2-xl lh-copy f4-l'}).text
                
            except:
                
                price = one_div.find('div',attrs = {'class':'b f5 f4-l black mr1 lh-copy'})
                

            print(price) 
            
            data={"link":link,"title":title,"price":price} 

            datainsert(data)   
            
            print("    "*5)

        print(len(parent_div))
            # spans=one_div.findAll('span',attrs = {'class':'w_Ap'}).text
            # print("=================")
                
















            # rate=one_div.findAll('div',attrs = {'class':'b f5 f4-l black mr1 lh-copy'}).text.replace('current price', '')
            # # price.append(rate)
            # print('PRICE',rate)
            # # for one_span in spans:
            # #     print("=================")
            # #     print(one_span)


            # # description.append(des)

            # for link in one_div.find('a',attrs = {'class':'absolute w-100 h-100 z-1 hide-sibling-opacity'}):
            #     l=link.get('href')
            #     print('Link', l)
            #     # prod_link.append(l)
            
            # # links=info.find_all('a')
            # # print('-------',links)
            # # print(links.get('href'))

except Exception as f:
    print(f)

# list = pd.DataFrame({ "Product Discription": description,"Price": price,"Product link":prod_link})

# df = pd.DataFrame.from_dict(list, orient='index')
# df = df.transpose()

# list.head(2)








# prod_des= soup.findAll('class',attrs= { 'class':'font-11 item-desc'})
# print(prod_des)



# print('888')
# print('pro',prod_des)
# print("###")

# for des in prod_des:
#     print('**42*')
#     name=des.h1.text

#     print(name)

#     # description=des.a.findAll('span', class_='w_B1').text
    
#     # print(description)
   
# page = requests.get("https://www.walmart.com/ip/Expert-Gardener-Organics-Vegetable-Tomato-Food-4-lb-Fertilizer-EG4TV/663680907?athcpid=663680907&athpgid=AthenaItempage&athcgid=null&athznid=si&athieid=v0&athstid=CS004&athguid=_Rkl44URJZqdL1GT8qf4HbaAw1aJgikqSMG2&athancid=null&athena=true")

# page
# print(page.status_code)

# # print(page.content)

# soup = BeautifulSoup(page.content, 'html.parser')    

# print(soup.prettify())
    

