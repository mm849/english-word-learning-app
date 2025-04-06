import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# OpenAI APIキーの設定とクライアントの初期化
client = OpenAI(api_key=api_key)

def get_word_info(word: str) -> tuple[str, str]:
    prompt = f"""
    以下の英単語について、日本語訳と英語の例文を簡潔に教えてください。

    単語: {word}

    フォーマット:
    日本語訳: （ここに日本語訳）
    例文: （ここに英語の例文）
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    content = response.choices[0].message.content.strip()

    # 簡易パース（例：日本語訳と例文に分ける）
    lines = content.splitlines()
    translation = ""
    example = ""
    for line in lines:
        if line.startswith("日本語訳"):
            translation = line.split(":", 1)[1].strip()
        elif line.startswith("例文"):
            example = line.split(":", 1)[1].strip()

    return translation, example



def generate_image(word: str) -> str:
    prompt = f"A high-quality illustration representing the word '{word}'"
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    image_url = response.data[0].url
    return image_url



import json
from pathlib import Path

SAVE_FILE = "word_data.json"

def save_card_to_json(word, translation, example, image_url):
    new_card = {
        "word": word,
        "translation": translation,
        "example": example,
        "image_url": image_url
    }

    data = []
    if Path(SAVE_FILE).exists():
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    data.append(new_card)

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)



st.title("英単語学習アプリ")
word = st.text_input("単語を入力してください")

if st.button("学習する"):
    if word:
        with st.spinner("学習中です…少々お待ちください"):
            # 意味・例文取得
            translation, example = get_word_info(word)

            # 画像生成
            image_url = generate_image(word)

            # 表示
            st.markdown(f"**日本語訳**: {translation}")
            st.markdown(f"**例文**: {example}")
            st.image(image_url, caption=f"{word} のイメージ", use_container_width=True)

            # 保存
            save_card_to_json(word, translation, example, image_url)

        st.success("この単語カードを保存しました ✅")
    else:
        st.warning("単語を入力してください。")
