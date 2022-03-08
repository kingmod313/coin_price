import os
import json
import random as rn
import time
import requests
keys = ['20712d3bd755cb52532f', '20712d3bd755cb52532f', '20712d3bd755cb52532f', '20712d3bd755cb52532f']

cha = ( rn.choice(keys) )


ipinfo4 = requests.get(f'https://free.currconv.com/api/v7/convert?q=USD_AFN&compact=ultra&apiKey={cha}')
zp = json.loads(ipinfo4.text)
l = zp['USD_AFN']

ipinfo1 = requests.get('https://free.currconv.com/api/v7/convert?q=IRR_AFN&compact=ultra&apiKey=20712d3bd755cb52532f')
z1 = json.loads(ipinfo1.text)
l1 = z1['IRR_AFN']
m = int("1000")
lol = l1*m

ipinfo1 = requests.get('https://free.currconv.com/api/v7/convert?q=PKR_AFN&compact=ultra&apiKey=20712d3bd755cb52532f')
z2 = json.loads(ipinfo1.text)
l2 = z2['PKR_AFN']
n = int("1000")
lo = l2*n

ipinfo3 = requests.get('https://free.currconv.com/api/v7/convert?q=EUR_AFN&compact=ultra&apiKey=20712d3bd755cb52532f')
z3 = json.loads(ipinfo3.text)
l3 = z3['EUR_AFN']


os.system("clear")


print(f"""

  \033[1;33m▄▄█▀▀▀▀▀█▄▄
▄█▀──▄─▄────▀█▄
█───▀█▀▀▀▀▄───█
█────█▄▄▄▄▀───█
█────█────█───█
▀█▄─▀▀█▀█▀──▄█▀
  ▀▀█▄▄▄▄▄█▀▀

\033[44mCoded By Murtaza\033[0;37m

  Exchange And Crypto Live Price

\033[46mWich Coin Do You Want To Get Price\033[0;37m

Doller to Afghani {l}

1000 Toman Iran To Afghani {lol}

1000 kaldar (PKR) To Afghani {lo}

Euro to Afghani {l3}

\033[0;42m E \033[0;37m=\033[0;34m Exchangerate Dollar
\033[0;42m 1 \033[0;37m=\033[0;33m Bitcoin
\033[0;42m 2 \033[0;37m=\033[0;31m Tron
\033[0;42m 3 \033[0;37m=\033[0;33m Dogecoin
\033[0;42m 4 \033[0;37m=\033[0;34m Litecoin
\033[0;42m 5 \033[0;37m=\033[0;36m Ethereum
\033[0;42m 6 \033[0;37m=\033[0;33m Binance Coin
\033[0;42m 7 \033[0;37m=\033[0;33m SHIB INU
\033[0;42m 8 \033[0;37m=\033[0;33m Solana

\033[45mADD MORE COIN SOON.....\033[0;37m

""")
ch = input("\033[0;37mCHOOSE YOUR CURRENCY : ")



if ch == "E" :
    ipinfo = requests.get('https://free.currconv.com/api/v7/convert?q=USD_AFN&compact=ultra&apiKey=20712d3bd755cb52532f')
    z = json.loads(ipinfo.text)
    l = z['USD_AFN']
    print(f" 1$ Dollar To Afghani is {l}")
    time.sleep(10.00)
    os.system("python coin_price.py")





if ch == "1" :
    ipinfo = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT')
    z = json.loads(ipinfo.text)
    l = z['price']
    print(f"""\033[0;33mBitcoin\033[0;34m :\033[0;33m (BTC) 
Price \033[0;34m: \033[0;37m{l} \033[0;33mUSD""")
    time.sleep(3.00)
    os.system("python coin_price.py")
elif ch == "2" :
    ipinfo = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=TRXUSDT')
    z = json.loads(ipinfo.text)
    l = z['price']
    print(f"""\033[0;33mTron\033[0;34m :\033[0;33m (TRX) 
Price \033[0;34m: \033[0;37m{l} \033[0;33mUSD""")
    time.sleep(3.00)
    os.system("python coin_price.py")
    
elif ch == "3" : 
    ipinfo = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=DOGEUSDT')
    z = json.loads(ipinfo.text)
    l = z['price']
    print(f"""\033[0;33mT33mDogecoin\033[0;34m :\033[0;33m (DOGE) 
Price \033[0;34m: \033[0;37m{l} \033[0;33mUSD""")
    time.sleep(3.00)
    os.system("python coin_price.py")
elif ch == "4" :
    ipinfo = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=LTCUSDT')
    z = json.loads(ipinfo.text)
    l = z['price']
    print(f"""\033[0;33mLitecoin\033[0;34m :\033[0;33m (LTC) 
Price \033[0;34m: \033[0;37m{l} \033[0;33mUSD""")
    time.sleep(3.00)
    os.system("python coin_price.py")

elif ch == "5" :
    ipinfo = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT')
    z = json.loads(ipinfo.text)
    l = z['price']
    print(f"""\033[0;33mEthereum\033[0;34m :\033[0;33m (ETH) 
Price \033[0;34m: \033[0;37m{l} \033[0;33mUSD""")
    time.sleep(3.00)
    os.system("python coin_price.py")

elif ch == "6" :
    ipinfo = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=BNBUSDT')
    z = json.loads(ipinfo.text)
    l = z['price']
    print(f"""\033[0;33mBinance coin\033[0;34m :\033[0;33m (BNB) 
Price \033[0;34m: \033[0;37m{l} \033[0;33mUSD""")
    time.sleep(3.00)
    os.system("python coin_price.py")

elif ch == "7" :
    ipinfo = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=SHIBUSDT')
    z = json.loads(ipinfo.text)
    l = z['price']
    print(f"""\033[0;33mSHIB Inu\033[0;34m :\033[0;33m (SHIB) 
Price \033[0;34m: \033[0;37m{l} \033[0;33mUSD""")
    time.sleep(3.00)
    os.system("python coin_price.py")
    
elif ch == "8" :
    ipinfo = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=SOLUSDT')
    z = json.loads(ipinfo.text)
    l = z['price']
    print(f"""\033[0;33m Solana \033[0;34m :\033[0;33m (SOL) 
Price \033[0;34m: \033[0;37m{l} \033[0;33mUSD""")
    time.sleep(3.00)
    os.system("python coin_price.py")
else :
   print(" Unknown Character ")
   os.system("python coin_price.py")
   
   


time.sleep(1.00)
os.system("python coin_price.py")


#ZERO
#TO
#HERO