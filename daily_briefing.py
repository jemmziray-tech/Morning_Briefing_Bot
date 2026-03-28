import os
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# Securely load your Telegram keys from GitHub Secrets
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def get_weather():
    """Fetches the live temperature specifically for Tengeru, Tanzania."""
    try:
        # Tengeru exact coordinates: Lat -3.37, Lon 36.79
        url = "https://api.open-meteo.com/v1/forecast?latitude=-3.37&longitude=36.79&current_weather=true"
        response = requests.get(url, timeout=10)
        data = response.json()
        temp = data["current_weather"]["temperature"]
        return f"🌡️ Tengeru Weather: {temp}°C"
    except Exception as e:
        print(f"Weather error: {e}")
        return "🌡️ Weather: Unavailable right now."


def fetch_rss_headlines(feed_url, limit=2):
    """A master function to secretly read any News RSS feed in the world."""
    try:
        # Request the raw XML data from the news site
        response = requests.get(feed_url, timeout=10)
        root = ET.fromstring(response.content)

        headlines = []
        # Find the top 'items' (news articles) in the feed
        for item in root.findall(".//item")[:limit]:
            title = item.find("title").text
            headlines.append(f"▪️ {title}")

        return "\n".join(headlines)
    except Exception as e:
        print(f"RSS Error for {feed_url}: {e}")
        return "▪️ Headlines currently unavailable."


def send_telegram_message(message_text):
    """Sends the final formatted message to your Telegram app."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message_text}

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Massive News & Weather Briefing successfully sent to your phone!")
    else:
        print(f"❌ Failed to send message: {response.text}")


if __name__ == "__main__":
    # 1. Get today's date
    today_date = datetime.now().strftime("%A, %B %d")

    # 2. Grab Weather for Tengeru
    weather = get_weather()

    # 3. Grab Live News via RSS (Pulling 2 headlines each)
    bbc_world = fetch_rss_headlines("http://feeds.bbci.co.uk/news/world/rss.xml", 2)
    cnn_world = fetch_rss_headlines("http://rss.cnn.com/rss/edition.rss", 2)
    bbc_africa = fetch_rss_headlines(
        "http://feeds.bbci.co.uk/news/world/africa/rss.xml", 2
    )

    # 4. Grab Sports News (Pulling 3 headlines for Sports!)
    sports = fetch_rss_headlines("http://feeds.bbci.co.uk/sport/rss.xml", 3)

    # 5. Grab BBC Learning English (6 Minute English Feed - Pulling just the latest 1)
    bbc_english = fetch_rss_headlines(
        "https://podcasts.files.bbci.co.uk/p02qtkki.rss", 1
    )

    # 6. Assemble the Master Briefing
    briefing_message = (
        f"🌅 Habari ya Asubuhi!\n"
        f"📅 {today_date}\n\n"
        f"{weather}\n\n"
        f"🌍 **BBC WORLD NEWS:**\n"
        f"{bbc_world}\n\n"
        f"🔴 **CNN HEADLINES:**\n"
        f"{cnn_world}\n\n"
        f"🌍 **AFRICA UPDATES:**\n"
        f"{bbc_africa}\n\n"
        f"⚽ **SPORTS ROUNDUP:**\n"
        f"{sports}\n\n"
        f"📚 **BBC LEARNING ENGLISH:**\n"
        f"Latest Lesson: \n{bbc_english}\n\n"
        f"Have a highly productive day in Tengeru! ☕🚀"
    )

    # 7. Deliver to your phone
    send_telegram_message(briefing_message)
