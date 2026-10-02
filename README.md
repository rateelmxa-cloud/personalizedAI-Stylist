# AI Stylist 👗

Personalized AI Stylist is a personal styling application that recommends an outfit based on the user's weather, schedule, wardrobe, and personal preferences.

The project combines information from different sources and uses AI to make a practical outfit recommendation.

## How It Works

The application:

1. Gets the current weather using the Open-Meteo API.
2. Gets today's schedule from Google Calendar.
3. Loads the user's wardrobe from a JSON file.
4. Filters out clothing that does not match the user's preferences.
5. Sends the relevant information to Gemini.
6. Gemini recommends an outfit using clothes from the user's wardrobe.
7. The recommendation is displayed through a Streamlit interface.

## Features

- 🌤️ Weather-based outfit recommendations
- 📅 Uses the user's Google Calendar schedule
- 👕 Uses the user's actual wardrobe
- 🎨 Takes personal style preferences into account
- 🤖 Uses Gemini for outfit reasoning
- 🖥️ Simple Streamlit user interface

## Technologies Used

- Python
- Streamlit
- Google Calendar API
- Open-Meteo API
- Google Gemini
- JSON

## Project Structure

```text
AI-Stylist/
├── app.py
├── stylist.py
├── wardrobe.json
├── .gitignore
└── README.md

### `app.py`

Contains the Streamlit interface for the application.

### `stylist.py`

Contains the main logic for:
- Getting weather information
- Getting the user's schedule
- Reading the wardrobe
- Filtering clothing based on preferences
- Generating the outfit recommendation with Gemini

### `wardrobe.json`

Stores the user's clothing items.

### `.gitignore`

Prevents private files such as Google authentication files from being uploaded to GitHub.

## Example

The application can consider information such as:

- Hot weather
- A university schedule
- Available clothing
- Preferred colors
- Preferred style

It then recommends an outfit using clothing available in the user's wardrobe.

## Future Improvements

Possible future improvements include:

- Adding clothing through the user interface
- Adding outfit images
- Improving wardrobe filtering
- Adding more detailed weather information
- Deploying the application online

## Author

Rateel
