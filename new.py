import os
import hashlib
from datetime import datetime, timezone, timedelta

def generate_md5_filename():
    # 現在の日付と時刻（ミリ秒を除いた）を取得
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # 日付と時刻をMD5ハッシュに変換してファイル名にする
    md5_hash = hashlib.md5(current_datetime.encode()).hexdigest()
    return f"{md5_hash}.md"

def create_md_file(directory):
    # ファイル名を生成
    filename = generate_md5_filename()
    # ファイルのパスを作成
    file_path = os.path.join(directory, filename)

    # ディレクトリが存在しない場合は作成する
    os.makedirs(directory, exist_ok=True)

    # 現在の日付と時刻（ミリ秒を除いた）を取得
    current_datetime = datetime.now(timezone.utc).replace(microsecond=0)
    
    # 現地時刻に変換
    jst = timezone(timedelta(hours=9))  # 日本時間のタイムゾーン
    current_datetime_jst = current_datetime.astimezone(jst)

    # フロントマターの内容を作成
    front_matter = f"""+++
title = '{filename}'
slug = '{filename}'
date = '{current_datetime_jst.isoformat()}'
type = 'tweet'
draft = false
+++\n\n"""

    # ファイルに書き込む
    with open(file_path, 'w') as file:
        file.write(front_matter)

    print(f"Markdown file '{filename}' generated successfully in '{directory}'.")

if __name__ == "__main__":
    target_directory = "content/tweets/"  # スクリプトの実行ディレクトリからの相対パス
    create_md_file(target_directory)
