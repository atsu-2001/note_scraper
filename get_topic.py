def select_topic(TOPIC_MAP):
    for i, topic in enumerate(TOPIC_MAP.keys(), 1):
        print(f"{i}. {topic}")

    while True:
        user_input = input('どのトピックを選択しますか')
        try:
            choice = int(user_input)
            if 1 <= choice <= len(TOPIC_MAP):
                return list(TOPIC_MAP.values())[choice - 1]
            else:
                print('範囲外の数字です')
        except ValueError:
            print('⚠️ 無効な入力です。数字を入力してください。')
