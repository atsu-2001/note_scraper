import time
from bs4 import BeautifulSoup
def add_body(top_5,browser):
    for i,item in enumerate(top_5):
        item_url = item['url']
        browser.get(item_url)
        time.sleep(3)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        try:
            body = soup.find('div', class_='note-common-styles__textnote-body').get_text(strip=True)
            body_200 = body[:200] + '...'
            top_5[i]['body'] = body_200
        except AttributeError:
            top_5[i]['body'] = '（本文取得エラー）'
