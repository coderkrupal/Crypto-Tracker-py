import requests
import json
import time
import pyfiglet


RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = "\033[0;35m"
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""
  {CYAN}                    
  
  
_________                        __           ___________                     __                 
\_   ___ \_______ ___.__._______/  |_  ____   \__    ___/___________    ____ |  | __ ___________ 
/    \  \/\_  __ <   |  |\____ \   __\/  _ \    |    |  \_  __ \__  \ _/ ___\|  |/ // __ \_  __ \
\     \____|  | \/\___  ||  |_> >  | (  <_> )   |    |   |  | \// __ \\  \___|    <\  ___/|  | \/
 \______  /|__|   / ____||   __/|__|  \____/    |____|   |__|  (____  /\___  >__|_ \\___  >__|   
        \/        \/     |__|                                       \/     \/     \/    \/       

  
  
  """

print(banner)


def Binance_show():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    price_data = response.json()
    print("#########################################################")
    print(f"Binance Price is:${price_data["price"]}")
    print("#########################################################")


def CoinGecko():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    price_data = response.json()
    print("#########################################################")
    print(f"CoinGecko Price is:${price_data["bitcoin"]["usd"]}")
    print("#########################################################")


def price_change_analysis():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,  # Fetch top 10 cryptocurrencies
        "page": 1,
        "sparkline": False,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return []


def analyze_price_changes(data):
    gainers = sorted(data, key=lambda x: x["price_change_percentage_24h"], reverse=True)
    losers = sorted(data, key=lambda x: x["price_change_percentage_24h"])

    print("\n📈 **Top 10 Cryptocurrencies** (24h Change) 📉")
    for coin in data:
        print(
            f"{coin['name']} ({coin['symbol'].upper()}) - Price: ${coin['current_price']} | 24h Change: {coin['price_change_percentage_24h']:.2f}%"
        )

    print("\n🚀 **Top 3 Gainers** 🚀")
    for coin in gainers[:3]:
        print(
            f"{coin['name']} ({coin['symbol'].upper()}) +{coin['price_change_percentage_24h']:.2f}%"
        )

    print("\n📉 **Top 3 Losers** 📉")
    for coin in losers[:3]:
        print(
            f"{coin['name']} ({coin['symbol'].upper()}) {coin['price_change_percentage_24h']:.2f}%"
        )


def main():
    print("1. Real-Time Cryptocurrency Price Tracking")
    print("2.Market Insights & Trends")
    print(" 3. Portfolio Management")
    print("4.Market Data ")
    user_choice = int(input("which feature you want to show"))
    if user_choice == 1:
        print("welcome to Real-Time Cryptocurrency Price Tracking")
        print("1.Binance Price")
        print("2.CoinGecko Price:")
        priceChoice = int(input("please select:"))
        if priceChoice == 1:
            Binance_show()
        elif priceChoice == 2:
            CoinGecko()

    elif user_choice == 2:
        print("welcome to Market Insights & Trends")
        print("1. Price Change Analysis")
        print("2.Volume & Market Cap Trends")
        print("3.Moving Averages & Trends")
        price_choice = int(input("please select:"))
        if price_choice == 1:
            crypto_data = price_change_analysis()
            if crypto_data:
                analyze_price_changes(crypto_data)

    elif user_choice == 3:
        print("welcome to Portfolio Management")
    elif user_choice == 4:
        print("Market Data")


if __name__ == "__main__":
    main()
