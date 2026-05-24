import smtplib
from email.mime.text import MIMEText
from src.config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_weather_alert(subject, message):

    msg = MIMEText(message)

    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(EMAIL_SENDER, EMAIL_PASSWORD)

    server.sendmail(
        EMAIL_SENDER,
        EMAIL_RECEIVER,
        msg.as_string()
    )

    server.quit()

    print("Alert Email Sent!")
