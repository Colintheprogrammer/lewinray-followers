import os
import requests
from datetime import datetime

RAPIDAPI_KEY = os.environ["RAPIDAPI_KEY"]
TIKTOK_USER_ID = "56605052018139136"

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

def format_number_spaced(number):
    return f"{number:,}".replace(",", " ")

def write_html_file(content):
    with open("tiktok.html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TikTok Followers</title>
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
      font-size: 4rem;
      color: black;
    }}
  </style>
</head>
<body>
  <div class="followers">{content}</div>
</body>
</html>""")

if __name__ == "__main__":
    formatted_followers = get_tiktok_followers_by_id(TIKTOK_USER_ID)
    write_html_file(formatted_followers)
