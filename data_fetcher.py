


import requests

def get_solana_token_profiles():
    url = "https://api.dexscreener.com/token-profiles/latest/v1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # اگر HTTP error بود، exception می‌ده
        data = response.json()
    except Exception as e:
        print("❌ JSON Error:", e)
        return []  # برگردوندن لیست خالی به‌جای None

    solana_tokens = [token for token in data if token.get("chainId") == "solana"]
    return solana_tokens