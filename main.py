import requests
import os
import argparse


API_KEY = os.environ["API_KEY"]
API_URL = "https://api.exchangeratesapi.io/v1/latest"
params = {
    'access_key': f'{API_KEY}',
}


def get_currency():
    currency = requests.get(f'{API_URL}', params=params)
    return currency


def exchange(amount, base_cur, target_cur):
    final_amount = (amount / base_cur) * target_cur
    return final_amount


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--amount", help="Amount of currency", required=True)
    ap.add_argument("-b", "--base", help="Base currency", required=True)
    ap.add_argument("-t", "--target", help="Target currency", required=True)
    args = ap.parse_args()

    cur = get_currency().json()
    print(round(exchange(int(args.amount), cur["rates"][f"{args.base}"], cur["rates"][f"{args.target}"]), 2))
