import requests
import json
import math

print("type keyword:")
keyword = input()
url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
}
# params = {
#     "op": "keyword"
# }

MAX_PAGES = None
SET = set()
RESULTS = []
PAGE_INDEX = 1

while True:
    data = {
        "cname": '',
        "pid": '',
        "keyword": keyword,
        "pageIndex": str(PAGE_INDEX),
        "page_size": '10'
    }
    resp = requests.post(url, headers=headers, data=data)
    try:
        parsed = resp.json()
    except Exception as e:
        print(f"Error parsing JSON: {e}")

    table = parsed.get('Table1', [])
    if not table:
        print("No more data available.")
        break

    for item in table:
        store = item.get('storeName')
        addr = item.get('addressDetail')
        key = f"{store}\u0000{addr}"
        if key in SET:
            continue
        else:
            SET.add(key)
            # Collect structured record; include other available fields if present
            record = {
                'storeName': store,
                'addressDetail': addr,
            }
            # optional fields
            if item.get('telephone'):
                record['telephone'] = item.get('telephone')
            if item.get('cityName'):
                record['cityName'] = item.get('cityName')
            RESULTS.append(record)
            print(f"{store}\t{addr}")

    if MAX_PAGES == None:
        try:
            row_nums = (parsed.get('Table',[{}])[0].get('rowcount',0))
            print(row_nums)
        except Exception as e:
            print(f"Error getting row count: {e}")
            row_nums = 0
        if row_nums > 10:
            MAX_PAGES = math.ceil(row_nums / 10)
            print(f"Total pages: {MAX_PAGES}")

    if PAGE_INDEX > MAX_PAGES:
        print("Reached the last page.")
        break

    PAGE_INDEX += 1


with open(f"./temp/KFC_{keyword}.json", 'w', encoding='utf-8') as f:
    json.dump(RESULTS, f, ensure_ascii=False, indent=2)