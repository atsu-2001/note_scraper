import sys


def create_top_5(soup,base_url):
    articles = soup.find_all('div', class_='m-largeNoteWrapper__card')
    if not articles:
        print("⚠️ 記事が見つかりませんでした。URLや構造を確認してください。")
        sys.exit()
    article_list = []
    for article in articles:
        try:
            title = article.find('h3', class_='m-noteBodyTitle__title').text.strip()
            article_url = article.find('a')['href']
            try:
                likes = int(article.find('span', class_='pl-2').text.strip())
            except (AttributeError, ValueError):
                likes = 0
            writer = article.find('span', class_='o-noteItem__userText').text.strip()
            article_list.append({
                "title": title,
                "url": base_url + article_url,
                "likes": likes,
                "writer": writer
            })
        except AttributeError as e:
            continue
    sort_list = sorted(article_list, key=lambda k: k['likes'], reverse=True)
    return sort_list[:5]
