import requests
import json
import time
import pyfiglet
import csv


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


#  1 Price Change Analysis
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


# finish

# market cap trends


def get_global_market_data():
    url = "https://api.coingecko.com/api/v3/global"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["data"]
        return data
    else:
        print("Error fetching global market data:", response.status_code)
        return None


def get_top_cryptos_by_volume():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",  # Sort by highest 24h volume
        "per_page": 5,  # Fetch top 5 coins by volume
        "page": 1,
        "sparkline": False,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching volume data:", response.status_code)
        return []


def display_market_insights():
    global_data = get_global_market_data()
    if global_data:
        print("\n🌍 **Global Market Trends** 🌍")
        print(f"Total Market Cap: ${global_data['total_market_cap']['usd']:,}")
        print(
            f"24h Market Cap Change: {global_data['market_cap_change_percentage_24h_usd']:.2f}%"
        )
        print(
            f"📌 Bitcoin Dominance: {global_data['market_cap_percentage']['btc']:.2f}%"
        )
        print(
            f"📌 Ethereum Dominance: {global_data['market_cap_percentage']['eth']:.2f}%"
        )

    cryptos = get_top_cryptos_by_volume()
    if cryptos:
        print("\n📊 **Top 5 Cryptos by 24h Trading Volume** 📊")
        for coin in cryptos:
            print(
                f"{coin['name']} ({coin['symbol'].upper()}) - Volume: ${coin['total_volume']:,}"
            )


# finish


# Function to fetch historical prices
def get_historical_prices(crypto_id, days=50):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
    params = {"vs_currency": "usd", "days": days, "interval": "daily"}

    try:
        response = requests.get(url, params=params)
        print("🔍 API Response Status Code:", response.status_code)  # Debugging step

        if response.status_code == 200:
            data = response.json()
            print("🔍 Raw API Response:", data)  # Print full API response for debugging

            # Ensure 'prices' key exists and contains data
            if "prices" in data and len(data["prices"]) > 0:
                return [entry[1] for entry in data["prices"]]  # Extract closing prices

        print("❌ Error: No data received from API or invalid response.")
    except requests.exceptions.RequestException as e:
        print("⚠️ Request failed:", str(e))
    finally:
        print("all complete")

    return []


def calculate_sma(prices, period):
    if len(prices) < period:
        return None  # Not enough data
    return sum(prices[-period:]) / period  # Average of last 'period' days


# maintenance code
# finish

#  csv file name decalre

filename = "profile.csv"


def main():
    print("1. Real-Time Cryptocurrency Price Tracking")
    print("2.Market Insights & Trends")
    print(" 3. Portfolio Management")
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
        elif price_choice == 2:
            display_market_insights()
        elif price_choice == 3:
            crypto_id = input("enter a crypto ID [EX:bitcoin]")
            crypto_days = int(input("enter days"))
            prices = get_historical_prices(crypto_id, crypto_days)
            if prices:
                sma_7 = calculate_sma(prices, 7)
                sma_50 = calculate_sma(prices, 50)

            print(f"\n📊 ${crypto_id} (BTC) Moving Averages 📊")
            print(f"Current Price: ${prices[-1]:,.2f}")
            print(f"7-day SMA: ${sma_7:,.2f}")
            print(f"50-day SMA: ${sma_50:,.2f}")

        # Trend Analysis
        if prices[-1] > sma_7:
            print("✅ Price above 7-day SMA: Short-term Uptrend")
        else:
            print("❌ Price below 7-day SMA: Short-term Downtrend")

        if prices[-1] > sma_50:
            print("✅ Price above 50-day SMA: Long-term Bullish Trend")
        else:
            print("❌ Price below 50-day SMA: Long-term Bearish Trend")
    elif user_choice == 3:
        print("welcome to Portfolio Management")
        print("1.add Cryptocurrnecy")
        print("2.check your profile")
        print("2.delete Cryptocurrnecy")
        port_choice = int(input("please select:"))
        if port_choice == 1:
            crypto_name = input("Enter Crypto Symbol:")
            crypto_ammount = input("Enter ammmount:")
            purchase_price = input("Enter Purchase Price (per unit):")
            portfolio = [f"${crypto_name},${crypto_ammount},${purchase_price}"]
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(portfolio)
            print(f"Data has been written to {filename}")

        if port_choice == 2:
            print("wait we are fetching your data......")
            rows = []
            time.sleep(5)
            with open(filename, mode="r", newline="") as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    rows.append(row)

                for row in rows:
                    print(", ".join(row))  # Print each row on one line

    elif user_choice == 4:
        print("Market Data")


if __name__ == "__main__":
    main()
