import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=ef592ccfde3fdb71deaaec5058fff686&symbols=USD,AUD,CAD,PLN,MXN&format=1")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
