import os
import requests

# === KONFIGURATION ===
RAPIDAPI_KEY = os.environ["RAPIDAPI_KEY"]

TIKTOK_USER_ID = "56605052018139136"
INSTAGRAM_PROFILE_URL = "https://www.instagram.com/lewinray/"
TWITCH_USERNAME = "lewinray"
YOUTUBE_URL = "https://www.youtube.com/@Lewinray"

# === HILFSMETHODEN ===
def format_number_spaced(number):
    return f"{number:,}".replace(",", " ")

# === TIKTOK ===
def get_tiktok_followers(user_id):
    url = "https://tiktok-scraper7.p.rapidapi.com/user/info"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
    }
    params = {"user_id": user_id}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return format_number_spaced(data["data"]["stats"]["followerCount"])

def write_tiktok_html(follower_count):
    with open("tiktok.html", "w", encoding="utf-8") as f:
        f.write(build_html(follower_count, "TikTok Followers"))

# === INSTAGRAM ===
def get_instagram_followers(profile_url):
    url = "https://instagram-statistics-api.p.rapidapi.com/community"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "instagram-statistics-api.p.rapidapi.com"
    }
    params = {"url": profile_url}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return format_number_spaced(data["data"]["usersCount"])

def write_instagram_html(follower_count):
    with open("instagram.html", "w", encoding="utf-8") as f:
        f.write(build_html(follower_count, "Instagram Followers"))

# === TWITCH ===
def get_twitch_followers(username):
    url = "https://twitch-scraper2.p.rapidapi.com/api/channels/info"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "twitch-scraper2.p.rapidapi.com"
    }
    params = {"channel": username}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return format_number_spaced(data["data"]["user"]["followers"]["totalCount"])

def write_twitch_html(follower_count):
    with open("twitch.html", "w", encoding="utf-8") as f:
        f.write(build_html(follower_count, "Twitch Followers"))

# === YOUTUBE ===
def get_youtube_subscribers(channel_url):
    url = "https://youtube138.p.rapidapi.com/channel/details/"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
    }
    params = {
        "id": channel_url,
        "hl": "en",
        "gl": "US"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return format_number_spaced(data["stats"]["subscribers"])

def write_youtube_html(subscriber_count):
    with open("youtube.html", "w", encoding="utf-8") as f:
        f.write(build_html(subscriber_count, "YouTube Subscribers"))

# === HTML TEMPLATE ===
def build_html(content, title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600&display=swap');
    body {{
      margin: 0;
      background-color: transparent;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }}
    .followers {{
      font-family: 'Inter', sans-serif;
      font-size: 18px;
      font-weight: bold;
      color: #9FA2A5;
      user-select: none;
    }}
  </style>
</head>
<body>
  <div class="followers">{content}</div>
</body>
</html>"""

# === AUSFÜHRUNG ===
if __name__ == "__main__":
    tt_followers = get_tiktok_followers(TIKTOK_USER_ID)
    insta_followers = get_instagram_followers(INSTAGRAM_PROFILE_URL)
    twitch_followers = get_twitch_followers(TWITCH_USERNAME)
    yt_subscribers = get_youtube_subscribers(YOUTUBE_URL)

    write_tiktok_html(tt_followers)
    write_instagram_html(insta_followers)
    write_twitch_html(twitch_followers)
    write_youtube_html(yt_subscribers)

    print("HTML-Dateien für TikTok, Instagram, Twitch und YouTube wurden erstellt.")
