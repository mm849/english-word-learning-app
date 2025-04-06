import streamlit as st
import json
from pathlib import Path

SAVE_FILE = "word_data.json"

st.title("📚 復習モード - 保存済み単語カード")

if Path(SAVE_FILE).exists():
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        try:
            cards = json.load(f)
        except json.JSONDecodeError:
            st.error("保存データが壊れているようです。")
            cards = []
else:
    st.info("まだ保存された単語はありません。")
    cards = []

if cards:
    for card in cards[::-1]:  # 新しい順に表示
        st.markdown(f"### 🔤 {card['word']}")
        st.markdown(f"**日本語訳**: {card['translation']}")
        st.markdown(f"**例文**: {card['example']}")
        st.image(card["image_url"], use_container_width=True)
        st.divider()
