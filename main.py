import sys
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common import WebDriverException
from get_topic import select_topic
from get_section import select_section
from get_top_5 import create_top_5
from get_body import add_body
from to_csv import save_csv
TOPIC_MAP = {
    "家庭": "livelihood",
    "フード": "gourmet",
    "ライフスタイル": "lifestyle",
    "ショッピング": "shopping",
    "育児": "childraising",
    "健康": "health",
    "旅行・おでかけ": "travel",
    "ペット": "pet",
    "コラム・エッセイ": "column",
    "美容": "beauty",
    "ファッション": "fashion",
    "DIY": "diy",
    "造形": "modelmold",
    "手芸": "handicraft",
    "アウトドア": "outdoor",
    "教育": "education",
    "読書": "reading",
    "デザイン": "design",
    "人文学": "humanities",
    "サイエンス": "science",
    "資格": "qualification",
    "ビジネス": "business",
    "キャリア": "career",
    "IT": "it",
    "経済・投資": "economy",
    "地域・行政": "local",
    "マンガ": "manga",
    "芸能": "entertainment",
    "映画・ドラマ": "movie",
    "音楽": "music",
    "ラジオ": "radio",
    "舞台": "stage",
    "ゲーム": "game",
    "スポーツ": "sports",
    "野球": "baseball",
    "サッカー": "soccer",
    "競馬": "keiba",
    "麻雀": "mahjong",
    "Vtuber": "vtuber",
    "アニメ・特撮": "anime",
    "テクノロジー": "tech",
    "ガジェット": "gadget",
    "AI": "ai",
    "プログラミング": "programming",
    "VR・AR": "vr",
    "3DCG": "3d",
    "恋愛": "love",
    "アート": "art",
    "創作": "creation",
    "小説": "novel",
    "写真": "photo",
    "乗り物": "vehicle",
    "ホビー・玩具": "toyhobby"
}
browser = None
base_url = 'https://note.com'
try:
    topic_url = select_topic(TOPIC_MAP)
    url = f'{base_url}/topic/{topic_url}'
    try:
        browser = webdriver.Chrome()
    except WebDriverException as e:
        print("❌ ブラウザの起動に失敗しました。ChromeDriverのパスやバージョンを確認してください。")
        print(f"エラー内容: {e}")
        sys.exit()
    browser.get(url)
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    section_url = select_section(soup)
    url = f'{base_url}/interests/{section_url}'
    browser.get(url)
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    top_5 = create_top_5(soup,base_url)
    add_body(top_5,browser)
    save_csv(top_5,section_url)
finally:
    if browser:
        browser.quit()
