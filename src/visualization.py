import pandas as pd
import matplotlib.pyplot as plt

def generate_chart():

    data = pd.read_csv("data/weather_history.csv")

    plt.figure(figsize=(10, 5))

    plt.plot(data["Date"], data["Temperature"])

    plt.xticks(rotation=45)

    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature °C")

    plt.tight_layout()

    plt.savefig("charts/temperature_chart.png")

    print("Chart Generated!")
