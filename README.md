# 英単語ビジュアル学習アプリ / English Vocabulary Visual Learning App

AIの力で、英単語を「意味＋例文＋イメージ画像」で視覚的に学習できるアプリです。
This app allows users to learn English vocabulary visually using AI-powered **meanings, example sentences, and generated images**.

日本のビジネスパーソンを対象に、短時間で直感的に単語を記憶・定着できるよう設計しました。
Designed for Japanese business professionals, the app helps users memorize words efficiently in a short time.

---

## 🔍 概要 / Overview

**対象ユーザー**：日本のビジネスパーソン
**Target User**: Japanese business professionals

**学習スタイル**：英単語を入力 → 意味・例文・画像を自動生成
**Learning Style**: Type in a word → Automatically generate meaning, example sentence, and image

**目的 / Purpose**:
- 忙しい社会人でも直感的に語彙を定着させられること
  Help busy professionals memorize vocabulary effectively

---

## ⚙️ 使用技術 / Tech Stack

| 分野 / Area        | 使用技術 / Tools              |
|-------------------|-------------------------------|
| 言語 / Language   | Python 3.11                   |
| UI                | Streamlit                     |
| AI API            | OpenAI (ChatGPT & DALL·E 3)   |
| 保存 / Storage    | JSON (MVP version)            |

---

## ✨ 機能一覧 / Features

- 単語を入力 → 意味・例文を取得（ChatGPT）
  Input a word and retrieve its Japanese meaning and English example sentence via ChatGPT
- 単語のイメージ画像を生成（DALL·E 3）
  Generate an image representing the word using DALL·E 3
- 単語カードを保存＆復習画面で表示
  Save word cards and review them in a separate page
- `st.spinner()`で処理中の表示
  Display "loading" spinner while fetching results
- `.env`でAPIキーを管理
  Manage OpenAI API key using `.env` file

---

## 🚀 実行方法 / How to Run Locally

### 1. リポジトリをクローン / Clone this repo
```bash
git clone https://github.com/yourname/english-word-learning-app.git
cd english-word-learning-app
```

### 2. ライブラリをインストール / Install requirements
```env
pip install -r requirements.txt
```

### 3. .env ファイルを作成し、OpenAI APIキーを記載 / Create .env with your API key
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. アプリを起動 / Launch the app
```bash
streamlit run app.py
```


---
## Directory Structure
```plaintext
english-word-learning-app/
├── app.py                ← メイン画面 / Main learning UI
├── pages/
│   └── 1_復習.py         ← 復習モード / Review page
├── word_data.json        ← 保存データ（.gitignore推奨）/ Saved data
├── .env.example
├── requirements.txt
└── README.md
```

--
## Future Improvements
- SQLite保存への移行 / Move from JSON to SQLite
- クイズ形式の復習 / Add quiz-style review mode
- お気に入り・ステータス管理機能 / Add favorites and learning status
- モバイル対応UI / Mobile-friendly interface
- デプロイ：Streamlit Cloud / Vercel / Hugging Face Spaces など
- Deployment to public cloud platforms
