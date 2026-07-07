import requests
from config import API_KEY


def convert_currency(amount, from_currency, to_currency):

    url = (f"https://v6.exchangerate-api.com/v6/"f"{API_KEY}/latest/{from_currency}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data["result"] != "success":
            return None

        exchange_rate = data["conversion_rates"][to_currency]

        converted_amount = amount * exchange_rate

        return {"rate": exchange_rate, "converted": converted_amount}

    except requests.exceptions.RequestException:
        return None