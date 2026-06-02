import os
import requests

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


status = send_discord_webhook(WEBHOOK_URL, "沒事, "測試)
            
