# #!/Users/xibxib/trade/venv/bin/python
# # main.py

# import os
# from dotenv import load_dotenv

# from data_fetcher import get_solana_token_profiles
# from telegram_bot import send_telegram_message
# from utils import format_token_info

# # 🔒 بارگذاری متغیرهای محیطی
# load_dotenv()

# def main():
#     BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
#     CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

#     solana_tokens = get_solana_token_profiles()
#     print(f"📌 تعداد توکن‌های سولانا: {len(solana_tokens)}")

#     for token in solana_tokens[:21]:
#         message = format_token_info(token)
#         result = send_telegram_message(BOT_TOKEN, CHAT_ID, message)
#         print("ارسال پیام:", result)

# if __name__ == "__main__":
#     main()



#!/usr/bin/env python3
# main.py

import os

from data_fetcher import get_solana_token_profiles
from telegram_bot import send_telegram_message
from utils import format_token_info

def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # 👈 دقت کن به نام جدید
    CHAT_ID = os.getenv("CHAT_ID")

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ BOT_TOKEN یا CHAT_ID تنظیم نشده‌اند.")
        return

    solana_tokens = get_solana_token_profiles()
    print(f"📌 تعداد توکن‌های سولانا: {len(solana_tokens)}")

    for token in solana_tokens[:5]:  # برای تست اولیه فقط ۵ تا بفرست
        message = format_token_info(token)
        print("📨 پیام تولید شده:", message)
        result = send_telegram_message(BOT_TOKEN, CHAT_ID, message)
        print("✅ ارسال پیام:", result)

if __name__ == "__main__":
    main()