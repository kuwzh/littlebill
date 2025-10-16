import requests

BASE_URL = "https://techtest.hiboutik.com/api"
AUTH = ("yanis@gmail.com", "12345")

def fetch_clients():
    r = requests.get(f"{BASE_URL}/customers/", auth=AUTH, timeout=10)
    r.raise_for_status()
    return r.json()

def fetch_ventes():
    r = requests.get(f"{BASE_URL}/sales/", auth=AUTH, timeout=10)
    r.raise_for_status()
    return r.json()
