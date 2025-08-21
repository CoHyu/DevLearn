import requests

if __name__ == "__main__":
    url = "https://osu.ppy.sh/beatmapsets?q=keys%3D4"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Cookie": "osu_session=eyJpdiI6IndHZ0NkNzQxeURlUEdRakR1ekxTL1E9PSIsInZhbHVlIjoiMUVyby9YSURIaSsxWGVZbk4xSVFob21FY3hEOFAwY3ZvU040aDNnMWUyNlZMc2pnanZ0N1pOY1NiblN3QzM0Nkp6TFVld3k0NDZuOTExUlVoT0VWMWR6VWFSUXpYSmZ4aHpaWitLd29vL1hzblJsN3JCMXM5VkM2eG9tWFY5dktPKzYySnF2WjFadnp6dWxTc2xIN0FBPT0iLCJtYWMiOiJkMjFjM2VhYmY0ZGZkNDYwYmJmZGMxODVhYmNhM2VmMzFiM2E2ZTMxNzg3YzM0ZGVkNWJmMGY2NTEzZDdjMDg0IiwidGFnIjoiIn0%3D"
    }
    resp = requests.get(url, headers=headers)
    try:
        with open("./temp/osu_new_songs.html", 'w', encoding="utf-8") as f:
            f.write(resp.text)
            print("Success!")
    except Exception as e:
        print(f"Error: {e}")