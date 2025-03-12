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


def main():
    print("1. Real-Time Cryptocurrency Price Tracking")
    print("2.Market Insights & Trends")
    print(" 3. Portfolio Management")
    print("4.Market Data ")


if __name__ == "__main__":
    main()
