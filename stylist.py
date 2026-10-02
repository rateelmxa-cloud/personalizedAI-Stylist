import requests
import json

from datetime import datetime, timedelta, timezone

from google import genai
client = genai.Client()

preferences = {
    "favorite_colors": ["white", "black", "blue", "brown"],
    "preferred_style": "clean and casual and classy",
    "avoid": ["cream", "nude", "purple"]
}
with open("wardrobe.json", "r") as file:
    wardrobe = json.load(file)

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 24.4539,
        "longitude": 54.3773,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

creds = Credentials.from_authorized_user_file(
    "token.json",
    SCOPES
)

service = build("calendar", "v3", credentials=creds)


def get_todays_schedule():

    uae = timezone(timedelta(hours=4))
    now = datetime.now(uae)

    start_of_day = now.replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0
    )

    start_of_tomorrow = start_of_day + timedelta(days=1)

    events_result = service.events().list(
        calendarId="primary",
        timeMin=start_of_day.isoformat(),
        timeMax=start_of_tomorrow.isoformat(),
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])

    schedule = []

    for event in events:
        start = event["start"].get(
            "dateTime",
            event["start"].get("date")
        )

        end = event["end"].get(
            "dateTime",
            event["end"].get("date")
        )

        schedule.append({
            "title": event.get("summary", "Untitled event"),
            "start": start,
            "end": end
        })

    return schedule

def get_suitable_clothes():

    suitable_clothes = []

    for item in wardrobe:
        if item["color"].lower() not in preferences["avoid"]:
            suitable_clothes.append(item)

    return suitable_clothes
def get_outfit():

    weather = get_weather()
    schedule = get_todays_schedule()
    suitable_clothes = get_suitable_clothes()

    prompt = f"""
You are an AI personal stylist.

Choose one complete outfit for the user.

Consider:
- The weather
- The user's schedule
- The clothes they own
- Their personal preferences

Rules:
- Only choose clothes from the suitable wardrobe.
- Never invent clothing the user does not own.
- Make sure the outfit is practical for the weather.
- Make sure it fits the user's schedule.
- Do not use colors the user wants to avoid.

WEATHER:
{weather}

SCHEDULE:
{schedule}

WARDROBE:
{suitable_clothes}

PREFERENCES:
{preferences}

Give your answer in this format:

OUTFIT:
Shirt: [item]
Pants: [item]
Shoes: [item]

WHY:
[Explain your choices.]
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
