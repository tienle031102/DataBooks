# -*- coding: utf-8 -*-
"""laydulieu.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BJsWmsbiAM_SaM7GyDRBdaAKC9W9mQIU

**Lấy dữ liệu trên sàng thương mại Tiki**
"""

import requests
import time
import random
import pandas as pd

# cookies = {
#     'TIKI_GUEST_TOKEN': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
#     'TOKENS': '{%22access_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22%2C%22expires_in%22:157680000%2C%22expires_at%22:1763654224277%2C%22guest_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22}',
#     'amp_99d374': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlpc1q6.b.i.t',
#     'amp_99d374_tiki.vn': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlp8817.3.1.1',
#     '_gcl_au': '1.1.559117409.1605974236',
#     '_ants_utm_v2': '',
#     '_pk_id.638735871.2fc5': 'b92ae025fbbdb31f.1605974236.1.1605975278.1605974236.',
#     '_pk_ses.638735871.2fc5': '*',
#     '_trackity': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
#     '_ga_NKX31X43RV': 'GS1.1.1605974235.1.1.1605975326.0',
#     '_ga': 'GA1.1.657946765.1605974236',
#     'ai_client_id': '11935756853.1605974227',
#     'an_session': 'zizkzrzjzlzizqzlzqzjzdzizizqzgzmzkzmzlzrzmzgzdzizlzjzmzqzkznzhzhzkzdzizhzdzizlzjzmzqzkznzhzhzkzdzizlzjzmzqzkznzhzhzkzdzjzdzhzqzdzizd2f27zdzjzdzlzmzmznzq',
#     'au_aid': '11935756853',
#     'dgs': '1605975268%3A3%3A0',
#     'au_gt': '1605974227146',
#     '_ants_services': '%5B%22cuid%22%5D',
#     '__admUTMtime': '1605974236',
#     '__iid': '749',
#     '__su': '0',
#     '_bs': 'bb9a32f6-ab13-ce80-92d6-57fd3fd6e4c8',
#     '_gid': 'GA1.2.867846791.1605974237',
#     '_fbp': 'fb.1.1605974237134.1297408816',
#     '_hjid': 'f152cf33-7323-4410-b9ae-79f6622ebc48',
#     '_hjFirstSeen': '1',
#     '_hjIncludedInPageviewSample': '1',
#     '_hjAbsoluteSessionInProgress': '0',
#     '_hjIncludedInSessionSample': '1',
#     'tiki_client_id': '657946765.1605974236',
#     '__gads': 'ID=ae56424189ecccbe-227eb8e1d6c400a8:T=1605974229:RT=1605974229:S=ALNI_MZFWYf2BAjzCSiRNLC3bKI-W_7YHA',
#     'proxy_s_sv': '1605976041662',
#     'TKSESSID': '8bcd49b02e1e16aa1cdb795c54d7b460',
#     'TIKI_RECOMMENDATION': '21dd50e7f7c194df673ea3b717459249',
#     'cto_bundle': 'V9Dkml9NVXNkQmJ6aEVLcXNqbHdjcVZoQ0l5RXpOMlRybjdDT0JrUnNxVXc2bHd0N2J3Y2FCdmZVQXdYY1QlMkJYUmxXSHZ2UEFwd3IzRHhzRWJYMlQlMkJsQjhjQlA1JTJCcExyRzlUQk5CYUdMdjl2STNQanVsa3cycHd3SHElMkJabnI3dzNhREpZcFVyandyM1d1QWpJbWYxT1UyWDdHZyUzRCUzRA',
#     'TIKI_RECENTLYVIEWED': '58259141',
#     '_ants_event_his': '%7B%22action%22%3A%22view%22%2C%22time%22%3A1605974691247%7D',
#     '_gat': '1',
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/nha-sach-tiki/c8322',
    'x-guest-token': 'NrvIUytC9BLbWEi3RHdAKfxG5VZYhFMn',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'limit': '10',
    'sort': 'top_seller',
    'category': '8322',
    'page': '1',
    'urlKey':  'nha-sach-tiki',
}

product_id = []
for i in range(1, 50):
    params['page'] = i
    response = requests.get('https://tiki.vn/api/v2/products', headers=headers, params=params)#, cookies=cookies)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('data'):
            product_id.append({'id': record.get('id')})
    # time.sleep(random.randrange(3, 10))

df = pd.DataFrame(product_id)
df.to_csv('product_id_ncds.csv', index=False)

import pandas as pd
import requests
import time
import random
from tqdm import tqdm

cookies = {
    'TIKI_GUEST_TOKEN': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
    'TOKENS': '{%22access_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22%2C%22expires_in%22:157680000%2C%22expires_at%22:1763654224277%2C%22guest_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22}',
    'amp_99d374': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlohtdv.3.2.5',
    'amp_99d374_tiki.vn': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlocds8.0.1.1',
    '_gcl_au': '1.1.559117409.1605974236',
    '_ants_utm_v2': '',
    '_pk_id.638735871.2fc5': 'b92ae025fbbdb31f.1605974236.1.1605974420.1605974236.',
    '_pk_ses.638735871.2fc5': '*',
    '_trackity': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
    '_ga_NKX31X43RV': 'GS1.1.1605974235.1.1.1605974434.0',
    '_ga': 'GA1.1.657946765.1605974236',
    'ai_client_id': '11935756853.1605974227',
    'an_session': 'zizkzrzjzlzizqzlzqzjzdzizizqzgzmzkzmzlzrzmzgzdzizlzjzmzqzkznzhzhzkzdzhzdzizlzjzmzqzkznzhzhzkzdzizlzjzmzqzkznzhzhzkzdzjzdzhzqzdzizd2f27zdzjzdzlzmzmznzq',
    'au_aid': '11935756853',
    'dgs': '1605974411%3A3%3A0',
    'au_gt': '1605974227146',
    '_ants_services': '%5B%22cuid%22%5D',
    '__admUTMtime': '1605974236',
    '__iid': '749',
    '__su': '0',
    '_bs': 'bb9a32f6-ab13-ce80-92d6-57fd3fd6e4c8',
    '_gid': 'GA1.2.867846791.1605974237',
    '_fbp': 'fb.1.1605974237134.1297408816',
    '_hjid': 'f152cf33-7323-4410-b9ae-79f6622ebc48',
    '_hjFirstSeen': '1',
    '_hjIncludedInPageviewSample': '1',
    '_hjAbsoluteSessionInProgress': '0',
    '_hjIncludedInSessionSample': '1',
    'tiki_client_id': '657946765.1605974236',
    '__gads': 'ID=ae56424189ecccbe-227eb8e1d6c400a8:T=1605974229:RT=1605974229:S=ALNI_MZFWYf2BAjzCSiRNLC3bKI-W_7YHA',
    'proxy_s_sv': '1605976041662',
    'TKSESSID': '8bcd49b02e1e16aa1cdb795c54d7b460',
    'TIKI_RECOMMENDATION': '21dd50e7f7c194df673ea3b717459249',
    '_gat': '1',
    'cto_bundle': 'i6f48l9NVXNkQmJ6aEVLcXNqbHdjcVZoQ0k2clladUF2N2xjZzJ1cjR6WG43UTVaRmglMkZXWUdtRnJTNHZRbmQ4SDAlMkZwRFhqQnppRHFxJTJCSEozZXBqRFM4ZHVxUjQ2TmklMkJIcnhJd3luZXpJSnBpcE1nJTNE',
    'TIKI_RECENTLYVIEWED': '58259141',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/nha-sach-tiki/c8322',
    'x-guest-token': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = (
    ('platform', 'web'),
    ('spid', 187266106)
)

def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['sku'] = json.get('sku')
    d['name'] = json.get('name')
    d['author'] = json.get('authors')[0].get('name') if json.get('authors') and isinstance(json.get('authors'), list) and len(json.get('authors')) > 0 else None
    d['categorie_name'] = json.get('categories').get('name')
    d['price'] = json.get('price')
    d['price_usd'] = json.get('price_usd')
    d['description'] = json.get('description')
    return d

df_id = pd.read_csv('product_id_ncds.csv')
p_ids = df_id.id.to_list()
print(p_ids)
result = []

for pid in tqdm(p_ids, total=len(p_ids)):
    response = requests.get('https://tiki.vn/api/v2/products/{}'.format(pid), headers=headers, params=params, cookies=cookies)

    if response.status_code == 200:
        try:
            data = response.json()
            print('Crawl data {} success !!!'.format(pid))
            result.append(parser_product(data))
        except requests.exceptions.JSONDecodeError:
            print(f"Warning: Skipping product ID {pid} due to JSONDecodeError.")
            print(f"Response content: {response.content}")
    else:
        print(f"Request failed for product ID {pid} with status code: {response.status_code}")
        print(f"Response content: {response.content}")

    # time.sleep(random.randrange(3, 5))
df_product = pd.DataFrame(result)
df_product.to_csv('crawled_data_ncds.csv', index=False)

"""**Lấy dữ liệu trên sàn thương mại
Lazada**
"""

import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
# Declare browser
driver = webdriver.Chrome('chromedriver.exe')

# Open URL
driver.get("https://www.lazada.vn/dien-thoai-di-dong/?page=1&spm=a2o4n.home.cate_1.1.1905e182tGDwoM")
sleep(random.randint(5,10))

# ================================ GET link/title
elems = driver.find_elements(By.CSS_SELECTOR , ".RfADt [href]")
title = [elem.text for elem in elems]
links = [elem.get_attribute('href') for elem in elems]

# ================================ GET price
elems_price = driver.find_elements(By.CSS_SELECTOR , ".aBrP0")
len(elems_price)
price = [elem_price.text for elem_price in elems_price]

df1 = pd.DataFrame(list(zip(title, price, links)), columns = ['title', 'price','link_item'])
df1['index_']= np.arange(1, len(df1) + 1)

# ================================GET discount

# elems_discount = driver.find_elements(By.CSS_SELECTOR , ".WNoq3")
# discount_all = [elem.text for elem in elems_discount]

elems_discount = driver.find_elements(By.CSS_SELECTOR , ".WNoq3 ._1m41m")
discount = [elem.text for elem in elems_discount]

elems_discountPercent = driver.find_elements(By.CSS_SELECTOR , ".WNoq3 .IcOsH")
discountPercent = [elem.text for elem in elems_discountPercent]

discount_list, discount_idx, discount_percent_list = [], [], []
for i in range(1, len(title)+1):
    try:
        discount = driver.find_element("xpath", "/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/div[{}]/div/div/div[2]/div[4]/span[1]/del".format(i))
        discount_list.append(discount.text)
        discount_percent = driver.find_element("xpath", "/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/div[{}]/div/div/div[2]/div[4]/span[2]".format(i))
        discount_percent_list.append(discount_percent.text)
        print(i)
        discount_idx.append(i)
    except NoSuchElementException:
        print("No Such Element Exception " + str(i))

df2 = pd.DataFrame(list(zip(discount_idx , discount_list, discount_percent_list)), columns = ['discount_idx', 'discount_list','discount_percent_list'])

df3 = df1.merge(df2, how='left', left_on='index_', right_on='discount_idx')

# ================================ GET location/countReviews

elems_countReviews = driver.find_elements(By.CSS_SELECTOR , "._6uN7R")
countReviews = [elem.text for elem in elems_countReviews]

df3['countReviews'] = countReviews

# ================================ GET more infor of each item
# list1 = []
# list1 = [1,2,3,4] + list1

driver.get(links[0])

elems_name = driver.find_elements(By.CSS_SELECTOR , ".middle")
name_comment = [elem.text for elem in elems_name]

elems_content = driver.find_elements(By.CSS_SELECTOR , ".item-content .content")
content_comment = [elem.text for elem in elems_content]

elems_skuInfo= driver.find_elements(By.CSS_SELECTOR , ".item-content .skuInfo")
skuInfo_comment = [elem.text for elem in elems_skuInfo]

elems_likeCount = driver.find_elements(By.CSS_SELECTOR , ".item-content .bottom .left .left-content")
like_count = [elem.text for elem in elems_likeCount]

df4 = pd.DataFrame(list(zip(name_comment , content_comment, skuInfo_comment, like_count)),
                   columns = ['name_comment', 'content_comment','skuInfo_comment', 'like_count'])
# df4['link_item'] = links[0]
df4.insert(0, "link_item", links[0])

# ================================ next pagination
next_pagination_cmt = driver.find_element("xpath", "/html/body/div[4]/div/div[10]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button[2]")
next_pagination_cmt.click()
sleep(random.randint(1,3))
close_btn = driver.find_element("xpath", "/html/body/div[7]/div[2]/div")
close_btn.click()


# ================================
count = 1
name_comment, content_comment, skuInfo_comment, like_count = [], [], [], []
while True:
    try:
        print("Crawl Page " + str(count))
        elems_name = driver.find_elements(By.CSS_SELECTOR , ".middle")
        name_comment = [elem.text for elem in elems_name] + name_comment

        elems_content = driver.find_elements(By.CSS_SELECTOR , ".item-content .content")
        content_comment = [elem.text for elem in elems_content] + content_comment

        elems_skuInfo= driver.find_elements(By.CSS_SELECTOR , ".item-content .skuInfo")
        skuInfo_comment = [elem.text for elem in elems_skuInfo] + skuInfo_comment

        elems_likeCount = driver.find_elements(By.CSS_SELECTOR , ".item-content .bottom .left .left-content")
        like_count = [elem.text for elem in elems_likeCount] + like_count

        next_pagination_cmt = driver.find_element("xpath", "/html/body/div[4]/div/div[10]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button[2]")
        next_pagination_cmt.click()
        print("Clicked on button next page!")
        sleep(random.randint(1,3))
        try:
            close_btn = driver.find_element("xpath", "/html/body/div[7]/div[2]/div")
            close_btn.click()
            print("Clicked on button exit!")
            sleep(random.randint(1,3))
        except ElementNotInteractableException:
            continue
        sleep(random.randint(1,3))
        count += 1
    except ElementNotInteractableException:
        print("Element Not Interactable Exception!")
        break

df4 = pd.DataFrame(list(zip(name_comment , content_comment, skuInfo_comment, like_count)),
                   columns = ['name_comment', 'content_comment','skuInfo_comment', 'like_count'])
# df4['link_item'] = links[0]
df4.insert(0, "link_item", links[0])


# Close browser
driver.close()

# =============================================================================


# ============================GET INFOMATION OF ALL ITEMS
def getDetailItems(link):
    driver.get(link)
    count = 1
    name_comment, content_comment, skuInfo_comment, like_count = [], [], [], []
    while True:
        try:
            print("Crawl Page " + str(count))
            elems_name = driver.find_elements(By.CSS_SELECTOR , ".middle")
            name_comment = [elem.text for elem in elems_name] + name_comment

            elems_content = driver.find_elements(By.CSS_SELECTOR , ".item-content .content")
            content_comment = [elem.text for elem in elems_content] + content_comment

            elems_skuInfo= driver.find_elements(By.CSS_SELECTOR , ".item-content .skuInfo")
            skuInfo_comment = [elem.text for elem in elems_skuInfo] + skuInfo_comment

            elems_likeCount = driver.find_elements(By.CSS_SELECTOR , ".item-content .bottom .left .left-content")
            like_count = [elem.text for elem in elems_likeCount] + like_count

            next_pagination_cmt = driver.find_element("xpath", "/html/body/div[4]/div/div[10]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button[2]")
            next_pagination_cmt.click()
            print("Clicked on button next page!")
            sleep(random.randint(1,3))
            try:
                close_btn = driver.find_element("xpath", "/html/body/div[7]/div[2]/div")
                close_btn.click()
                print("Clicked on button exit!")
                sleep(random.randint(1,3))
            except ElementNotInteractableException:
                continue
            sleep(random.randint(1,3))
            count += 1
        except ElementNotInteractableException:
            print("Element Not Interactable Exception!")
            break

    df4 = pd.DataFrame(list(zip(name_comment , content_comment, skuInfo_comment, like_count)),
                       columns = ['name_comment', 'content_comment','skuInfo_comment', 'like_count'])
    # df4['link_item'] = links[0]
    df4.insert(0, "link_item", link)
    return df4

df_list = []
for link in links:
    df = getDetailItems(link)
    df_list.append(df)