from datetime import datetime
import os
import pandas as pd


def save_csv(top_5,section_url):
    today = datetime.today().strftime('%Y.%m.%d')
    df = pd.DataFrame(top_5)
    df.index = df.index + 1
    file_path = f'output/note_{section_url}_{today}.csv'
    try:
        df.to_csv(file_path, encoding='utf-8')
        print(f'csvに保存しました:{file_path}')
    except FileNotFoundError:
        print("📂 'output' フォルダが見つかりません。フォルダを作成します...")
        try:
            os.makedirs('output', exist_ok=True)
            df.to_csv(file_path, encoding='utf-8')
            print('✅ フォルダを作成し、CSVに保存しました:', file_path)
        except Exception as e:
            print(f"❌ 再保存にも失敗しました: {e}")

    except OSError as e:
        print(f"❌ ファイル名に使用できない文字がある可能性があります。エラー内容: {e}")
    except Exception as e:
        print(f"❌ 予期しないエラーが発生しました: {e}")
