import os
import requests
from datetime import datetime

RAPIDAPI_KEY = os.environ["RAPIDAPI_KEY"]
TIKTOK_USER_ID = "56605052018139136"
INSTAGRAM_USERNAME = "lewinray"

def format_number_spaced(number):
    return f"{number:,}".replace(",", " ")

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

def get_instagram_followers_by_username(username):
    url = "https://instagram-statistics-api.p.rapidapi.com/profile"
    querystring = {"url": f"https://www.instagram.com/{username}/"}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "instagram-statistics-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    data = response.json()
    return format_number_spaced(data["data"]["usersCount"])

def write_html_file(tiktok_count, insta_count):
    with open("followers.html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Followers</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600&display=swap');
    body {{
      margin: 0;
      background-color: transparent;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      gap: 80px;
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
  <div class="followers">{tiktok_count}</div>
  <div class="followers">{insta_count}</div>
</body>
</html>""")

if __name__ == "__main__":
    tiktok_followers = get_tiktok_followers_by_id(TIKTOK_USER_ID)
    instagram_followers = get_instagram_followers_by_username(INSTAGRAM_USERNAME)
    write_html_file(tiktok_followers, instagram_followers)
