import requests
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from money_parser import price_str
from dotenv import dotenv_values

url = "https://www.emag.ro/drujba-motofierastrau-cu-lant-pe-benzina-husqvarna-372xp-5-5-cp-71-cc-lungime-lama-45-cm-965968118/pd/DM51HVBBM/"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

google_app_password = dotenv_values(".env").get("GOOGLE_APP_PASSWORD")


def chainsaw_price():
    return float(price_str(bs.find("p", "product-new-price").text))  # type: ignore


def chainsaw_name():
    return bs.find("h1", "page-title").text.strip()  # type: ignore


def chainsaw_review():
    return bs.find("p", "review-rating-data").text.strip()  # type: ignore


print(f"chainsaw name: {chainsaw_name()}")
print(f"chainsaw price: {chainsaw_price()}")
print(f"chainsaw review: {chainsaw_review()}")


def send_email():
    msg = MIMEText(f"Whatever: {chainsaw_price()}")
    msg["Subject"] = "whatever subject"
    msg["From"] = "daniel.alistar97@gmail.com"
    msg["To"] = "daniel.baltag97@gmail.com"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login("daniel.alistar97@gmail.com", google_app_password)  # type: ignore
        smtp_server.sendmail(
            "daniel.alistar97@gmail.com", "daniel.baltag97@gmail.com", msg.as_string()
        )
    print("Message sent!")


send_email()
