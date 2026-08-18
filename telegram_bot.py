# ==========================================================================
# SMART TRADING AI — Telegram Signal Auto-Broadcast Bot
# ==========================================================================

import requests
import json
import time

# --- CONFIGURATION ---
TELEGRAM_BOT_TOKEN = "8996408216:AAEpZdCf3Jp0Vwg4H929qa2U6f32XejprGI"
TELEGRAM_CHAT_ID = ""  # Replace with your channel username (e.g. @my_channel) or chat ID

def broadcast_signal(symbol, signal_type, entry, sl, tp1, tp2, win_rate, rrr):
    """Formats and posts an AI trade signal directly to your Telegram Channel."""
    message = f"""
<b>🚀 SMART TRADING AI — NEW TRADE SETUP</b>

<b>Symbol:</b> <code>{symbol}</code>
<b>Signal:</b> <b>{signal_type}</b>

📌 <b>Entry Zone:</b> <code>${entry}</code>
🔴 <b>Stop Loss (SL):</b> <code>${sl}</code>
🟢 <b>Take Profit 1:</b> <code>${tp1}</code>
🟢 <b>Take Profit 2:</b> <code>${tp2}</code>

📊 <b>Win Rate:</b> <code>{win_rate}%</code>
⚖️ <b>Risk/Reward Ratio:</b> <code>1:{rrr}</code>

<i>🤖 Generated live by Smart Trading AI (Claude 3.5 Sonnet Engine)</i>
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, json=payload)
        res_data = response.json()
        if res_data.get("ok"):
            print("✅ Signal broadcasted successfully to Telegram!")
        else:
            print(f"❌ Telegram API Error: {res_data.get('description')}")
    except Exception as e:
        print(f"❌ Network Error: {e}")

if __name__ == "__main__":
    print(f"🤖 Smart Trading Telegram Bot initialized with token {TELEGRAM_BOT_TOKEN[:10]}...")
    # Example Test Broadcast:
    # broadcast_signal("BTCUSDT", "BUY (LONG)", "64350.00", "63800.00", "65100.00", "65900.00", "82.4", "2.65")
