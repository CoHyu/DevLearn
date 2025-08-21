import requests
import json

print("type in what you wanna to translate:")
keyword = input()
url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
data = {
    "kw": keyword
}

resp = requests.post(url, headers=headers, data=data)
try:
    parsed = resp.json()
    with open("./temp/baidu_translate_result.json", 'w', encoding="utf-8") as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)
        print("Success!")
except Exception as e:
    print(f"Error: {e}")