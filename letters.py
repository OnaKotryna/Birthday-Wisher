import random

from logger import logging
from data.data import NAME

def get_letter_text():
    random_letter = f"letter_{random.randrange(1,4)}.txt"
    logging.info(f"Chosen letter: {random_letter}")
    with open(f"./letter_templates/{random_letter}", "r") as file:
        letter_text = file.read()
    return letter_text


def replace_names(text, receiver):
    text = text.replace("[YOUR_NAME]", NAME)
    text = text.replace("[NAME]", receiver)
    logging.info(f"Formatted text: {text}")
    return text
