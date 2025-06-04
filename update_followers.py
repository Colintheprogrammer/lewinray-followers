import os
import requests
from datetime import datetime

def format_number_spaced(number):
    return f"{number:,}".replace(",", " ")

def get_tiktok_followers_by_id(user_id):
    url = f"https://tiktok-scraper7.p.rapidapi.com/user/detail?user_id={user_id}"
    headers = {
        "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
        "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return format_number_spaced(data["user"]["stats"]["followerCount"])

def write_html_file(content):
    html = f"""<!DOCTYPE html>
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
    <div class="followers">{content}</div>
</body>
</html>
"""
    with open("tiktok.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    tiktok_user_id = "56605052018139136"  # Deine TikTok-User-ID
    tt_followers = get_tiktok_followers_by_id(tiktok_user_id)
    write_html_file(tt_followers)
