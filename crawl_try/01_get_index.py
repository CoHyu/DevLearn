import requests

url = "https://wz.sun0769.com/political/index/politicsNewest"
resp = requests.get(url)

try:
    with open("1.html", 'w', encoding="utf-8") as f:
        f.write(resp.text)
except Exception as e:
    print("Error")

print("Success!")