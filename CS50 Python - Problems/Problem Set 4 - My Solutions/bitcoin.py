import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    bitCoinPrice = data['bpi']['USD']['rate_float']

    wantedBitCoin = float(input(""))
    bitCoins = wantedBitCoin * bitCoinPrice
    

    print(f"${bitCoins:,.4f}")

except requests.RequestException:
    print("Failed to acess the API")

except ValueError:
    print("Command-line argument is not a number")

except EOFError:
    print("Missing command-line argument  ")