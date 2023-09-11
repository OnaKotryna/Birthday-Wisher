from data.data import get_todays_birthdays
from letters import get_letter_text, replace_names
from emails import send_email
from logger import logging


def main():
    birthdays = get_todays_birthdays()
    for birthday in birthdays:
        logging.info(f"Send birthday wishes to: {birthday['name']}")
        letter_text = get_letter_text()
        letter_text = replace_names(letter_text, birthday["name"])
        send_email(birthday["email"], letter_text)


main()