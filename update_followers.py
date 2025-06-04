import os
import requests
from datetime import datetime

# --------------------
# Helferfunktion für HTML-Zahl mit Leerzeichen
# --------------------
def format_number_spaced(number):
    return "{:,}".format(int(number)).replace(",", " ")

# --------------------
# YouTube API-Abfrage
# --------------------
def get_youtube_followers(api_key, channel_id):
    url = (
        f"https://www.googleapis.com/youtube/v3/channels"
        f"?part=statistics&id={channel_id}&key={api_key}"
    )
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return format_number_spaced(data["items"][0]["statistics"]["subscriberCount"])

# --------------------
# TikTok API via RapidAPI
# --------------------
def get_tiktok_followers_by_id(user_id):
    url = f"https://tiktok-scraper7.p.rapidapi.com/user/followers?user_id={user_id}&count=1&time=0"
    headers = {
        "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
        "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return format_number_spaced(data["data"]["followers"][0]["follower_count"])

# --------------------
# HTML-Datei erstellen
# --------------------
def create_html(filename, formatted_number):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{filename}</title>
</head>
<body style="background-color: transparent; display: flex; justify-content: center; align-items: center; height: 100vh;">
  <div style="font-size: 64px; font-weight: bold; color: black;">
    {formatted_number}
  </div>
</body>
</html>""")

# --------------------
# Hauptablauf
# --------------------
if __name__ == "__main__":
    youtube_api_key = os.environ["YOUTUBE_API_KEY"]
    youtube_channel_id = "UCTdvynmLeTfcaqc4k40b-dA"  # <- Dein YT-Channel
    tiktok_user_id = "56605052018139136"  # <- Dein TikTok-User-ID

    yt_followers = get_youtube_followers(youtube_api_key, youtube_channel_id)
    tt_followers = get_tiktok_followers_by_id(tiktok_user_id)

    create_html("youtube.html", yt_followers)
    create_html("tiktok.html", tt_followers)

    # Optional: Weitere Plattformen statisch
    create_html("instagram.html", "1 200 000")
    create_html("twitch.html", "850 000")

    print("✅ Follower-Seiten aktualisiert.")
