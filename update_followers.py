import requests
import os
from datetime import datetime

# YouTube API (live)
API_KEY = os.environ["YOUTUBE_API_KEY"]
CHANNEL_ID = "UCTdvynmLeTfcaqc4k40b-dA"

def get_youtube_subscribers():
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    subs = int(data["items"][0]["statistics"]["subscriberCount"])
    return str(subs)

# TikTok API via RapidAPI – mit täglichem Cache
def get_tiktok_followers_by_id(user_id):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    cache_file = "tiktok_cache.txt"

    # 🔁 Wenn heute schon gespeichert wurde → aus Datei lesen
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            line = f.readline().strip()
            if line.startswith(today):
                return line.split(",")[1]

    # 📡 Sonst von API abrufen
    url = f"https://tiktok-scraper7.p.rapidapi.com/user/followers?user_id={user_id}&count=100&time=0"
    headers = {
        "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
        "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    count = str(data["data"]["total"])

    # 💾 Speichern fürs nächste Mal
    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(f"{today},{count}")
    return count

# 🔤 HTML-Datei schreiben (nur Zahl zentriert anzeigen)
def write_html(filename, number_only):
    html = f"""<!DOCTYPE html>
<html lang='de'>
<head>
  <meta charset='UTF-8'>
  <style>
    body {{
      margin: 0;
      padding: 0;
      font-size: 2rem;
      color: white;
      background: transparent;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      font-family: sans-serif;
    }}
  </style>
</head>
<body>
  {number_only}
</body>
</html>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

# ▶️ Start
if __name__ == "__main__":
    yt_subs = get_youtube_subscribers()
    write_html("youtube.html", yt_subs)

    tt_followers = get_tiktok_followers_by_id("56605052018139136")  # ← DEINE TikTok-User-ID
    write_html("tiktok.html", tt_followers)

    write_html("instagram.html", "329800")  # noch statisch
    write_html("twitch.html", "8810")       # noch statisch
