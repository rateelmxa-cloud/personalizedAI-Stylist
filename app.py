import streamlit as st
from stylist import get_outfit

st.title("✨ Your  AI Stylist")
st.write("Your personal AI assistant that will pick your outfit based off your schedule and the weather and any other inconvinience so that your day runs smoothly!")
st.divider()

# Create two columns
weather_col, schedule_col = st.columns(2)

# Weather section
with weather_col:
    st.subheader("🌤️ Today's Weather")
    st.write("35°C")
    st.write("Feels like 38°C")
    st.write("Humidity: 55%")

# Schedule section
with schedule_col:
    st.subheader("📅 Today's Schedule")
    st.write("🎓 University")
    st.write("🏋️ Gym")

st.divider()
# Outfit button
if st.button("🦢Get Today's Outfit"):
    outfit = get_outfit()
    st.write(outfit)