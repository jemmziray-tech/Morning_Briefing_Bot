# ☕ Morning Briefing Bot (Personal ETL Assistant)

An automated Python script that acts as a personal digital assistant. It extracts live weather data and global news headlines, formats them into a daily briefing, and delivers them directly to a mobile device via Telegram every morning.

## 🚀 Features
* **Automated Scheduling:** Runs completely in the cloud using GitHub Actions (cron jobs).
* **Live Weather Data:** Extracts exact, localized temperature data using the Open-Meteo API.
* **RSS News Aggregation:** Scrapes live XML feeds from global news sources (BBC World, CNN, BBC Africa).
* **Sports & Education:** Pulls the latest sports headlines and the daily BBC Learning English podcast.
* **Instant Delivery:** Transforms the data into a clean UI and pushes it to a mobile device via the Telegram Bot API.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Automation:** GitHub Actions (CI/CD)
* **APIs:** Telegram Bot API, Open-Meteo API
* **Libraries:** `requests`, `xml.etree.ElementTree`, `os`, `datetime`

## ⚙️ Architecture (ETL Pipeline)
1. **Extract:** Python pings external APIs and RSS feeds to gather raw JSON and XML data.
2. **Transform:** The data is parsed, cleaned, and formatted into a readable, emoji-rich text string.
3. **Load:** An HTTP POST request pushes the final payload to the Telegram servers for immediate user delivery.
