import requests
import os

API_KEY = os.environ["YOUTUBE_API_KEY"]
CHANNEL_ID = "UCTdvynmLeTfcaqc4k40b-dA"

def get_youtube_subscribers():
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    subs = int(data["items"][0]["statistics"]["subscriberCount"])
    return f"{subs:,}".replace(",", ".") + " Abonnenten"

def write_html(filename, platform, value):
    html = f"""<!DOCTYPE html>
<html lang='de'>
<head><meta charset='UTF-8'><title>{platform} Follower</title></head>
<body style='font-family:sans-serif; text-align:center; padding:50px;'>
    <h2>{platform} Followerzahlen</h2>
    <p><strong>{platform}:</strong> {value}</p>
</body>
</html>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    yt_subs = get_youtube_subscribers()
    write_html("youtube.html", "YouTube", yt_subs)
    write_html("tiktok.html", "TikTok", "2.701.000 Follower")
    write_html("instagram.html", "Instagram", "329.800 Follower")
    write_html("twitch.html", "Twitch", "8.810 Follower")
