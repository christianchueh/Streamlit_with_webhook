import os
import requests
import streamlit as st

# ==========================================
# 1. 定義發送 Discord Webhook 的功能
# ==========================================
def send_discord_webhook(webhook_url, title, content):
    """直接發送漂亮的卡片訊息到 Discord"""
    payload = {
        "content": "📢 **來自 Streamlit 網頁的即時通知！**",
        "embeds": [
            {
                "title": f"🚀 {title}",
                "description": content,
                "color": 5763719,  # 綠色邊條 (十進位顏色碼)
                "footer": {
                    "text": "由 Streamlit 按鈕手動觸發"
                }
            }
        ]
    }
    
    # 發送 POST 請求給 Discord
    response = requests.post(webhook_url, json=payload)
    return response.status_code

# ==========================================
# 2. 設計 Streamlit 網頁版面
# ==========================================
st.set_page_config(page_title="Discord 通知控制台", page_icon="🚀")

st.title("Discord Webhook 測試控制台")
st.subheader("不用經過資料庫，按鈕點下去直接送出！")

# 🔒 安全對策：從環境變數讀取 Discord Webhook 網址
# 本地測試時，可以在 .streamlit/secrets.toml 設定
# 部署到 Streamlit Cloud 時，請在後台的 Secrets 設定
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# 讓使用者在網頁上輸入想要送出的標題與內容
input_title = st.text_input("請輸入通知標題：", value="測試通知")
input_content = st.text_area("請輸入通知內容：", value="這是一則從 Streamlit 網頁直接觸發的 Discord 訊息！")

st.divider() # 畫一條分隔線

# 🎯 核心功能：畫面上的發送按鈕
if st.button("🚀 點我立馬發送通知到 Discord"):
    if not WEBHOOK_URL:
        st.error("❌ 找不到 Discord Webhook 網址！請確保您已在 Streamlit 的 Secrets 中設定 `DISCORD_WEBHOOK_URL`。")
    else:
        with st.spinner("正在將訊息打包衝向 Discord..."):
            status = send_discord_webhook(WEBHOOK_URL, input_title, input_content)
            
            if status == 204:
                st.success("🟢 發送成功！快去你的 Discord 頻道看看有沒有跳出訊息！")
            else:
                st.error(f"🔴 發送失敗，Discord 回傳狀態碼：{status}")
