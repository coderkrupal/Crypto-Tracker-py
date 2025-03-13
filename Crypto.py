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
    elif user_choice == 3:
        print("welcome to Portfolio Management")
    elif user_choice == 4:
        print("Market Data")


if __name__ == "__main__":
    main()
