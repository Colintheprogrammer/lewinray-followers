import requests
import os
from datetime import datetime

# Format: 2 743 986 statt 2743986
def format_number_spaced(number: int) -> str:
    return f"{number:,}".replace(",", " ")

def get_tiktok_followers_by_id(user_id: str) -> int:
    url = f"https://tiktok-scraper7.p.rapidapi.com/user/followers?user_id={user_id}&count=1&time=0"

    headers = {
        "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
        "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Zugriff auf den ersten Follower-Eintrag
    return data["data"]["followers"][0]["follower_count"]

if __name__ == "__main__":
    tiktok_user_id = "56605052018139136"  # Deine TikTok User ID
    tt_followers = get_tiktok_followers_by_id(tiktok_user_id)
    formatted = format_number_spaced(tt_followers)

    with open("tiktok.html", "w", encoding="utf-8") as f:
        f.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TikTok Followers</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600&display=swap');
    body {{
      margin: 0;
      background-color: #1c1c1c;
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
  <div class="followers">{formatted}</div>
</body>
</html>
        """)
