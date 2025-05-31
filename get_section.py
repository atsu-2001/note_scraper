def select_section(soup):
    section_titles = soup.find_all('h2', attrs={'class': 'o-sectionHeadline__title'})
    for i, section_title in enumerate(section_titles, 1):
        print(f'{i}:{section_title.text}')

    while True:
        user_input = input('どのセクションを選択しますか : ')
        try:
            choice = int(user_input)
            if 1 <= choice <= len(section_titles):
                return section_titles[choice - 1].text
            else:
                print('範囲外の数字です')
        except ValueError:
            print('⚠️ 無効な入力です。数字を入力してください。')
