import os
import pandas as pd
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
NAME = os.getenv("NAME")
BIRTHDAYS = os.getenv("BIRTHDAYS_PATH")

def get_data():
    return pd.read_csv(BIRTHDAYS).to_dict(orient="records")


def get_todays_birthdays():
    today = dt.datetime.now()
    month = today.month
    day = today.day
    birthdays = []
    birthdays_data = get_data()
    for birthday in birthdays_data:
        if birthday["month"] == month and birthday["day"] == day:
            birthdays.append(birthday)
    return birthdays
