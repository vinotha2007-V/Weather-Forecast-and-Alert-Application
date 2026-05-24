import pandas as pd
from datetime import datetime

from src.weather_api import get_weather
from src.alert_system import send_weather_alert
from src.visualization import generate_chart

CITY = "Chennai"

def weather_job():

    data = get_weather(CITY)

    if data:

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print(f"\nWeather in {CITY}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather}")

        record = {
            "Date": datetime.now(),
            "Temperature": temperature,
            "Humidity": humidity
        }

        df = pd.DataFrame([record])

        df.to_csv(
            "data/weather_history.csv",
            mode="a",
            header=False,
            index=False
        )

        generate_chart()

        # Severe weather alert
        if temperature > 40:
            send_weather_alert(
                "High Temperature Alert!",
                f"Temperature reached {temperature}°C in {CITY}"
            )

    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    weather_job()
