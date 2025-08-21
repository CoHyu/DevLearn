import requests

print("Key in what you want to search:")
keyword = input()

url = "https://www.sogou.com/web"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
params = {
    "query": keyword
}

resp = requests.get(url, headers=headers, params=params)
fileName = keyword + ".html"

try:
    with open (fileName, 'w', encoding="utf-8") as f:
        f.write(resp.text)
        print("Success.")
except Exception as e:
    print(f"Sth wrong: {e}")