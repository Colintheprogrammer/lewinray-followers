import os
import requests
from datetime import datetime

RAPIDAPI_KEY = os.environ["RAPIDAPI_KEY"]

# TikTok
TIKTOK_USER_ID = "56605052018139136"

# Instagram
INSTAGRAM_PROFILE_URL = "https://www.instagram.com/lewinray/"


def get_tiktok_followers_by_id(user_id):
    url = "https://tiktok-scraper7.p.rapidapi.com/user/info"
    querystring = {"user_id": user_id}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    data = response.json()
    return format_number_spaced(data["data"]["stats"]["followerCount"])


def get_instagram_followers_by_url(profile_url):
    url = "https://instagram-statistics-api.p.rapidapi.com/profile"
    querystring = {"url": profile_url}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "instagram-statistics-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    data = response.json()
    return format_number_spaced(data["data"]["usersCount"])


def format_number_spaced(number):
    return f"{number:,}".replace(",", " ")


def write_html_file(content, filename="followers.html", platform="Followers"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{platform}</title>
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
    }}
  </style>
</head>
<body>
  <div class="followers">{content}</div>
</body>
</html>""")


if __name__ == "__main__":
    # TikTok
    tiktok_followers = get_tiktok_followers_by_id(TIKTOK_USER_ID)
    write_html_file(tiktok_followers, filename="tiktok.html", platform="TikTok Followers")

    # Instagram
    insta_followers = get_instagram_followers_by_url(INSTAGRAM_PROFILE_URL)
    write_html_file(insta_followers, filename="instagram.html", platform="Instagram Followers")
