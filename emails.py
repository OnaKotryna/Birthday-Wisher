import smtplib
from logger import logging
from data.data import PASSWORD, EMAIL

def send_email(addr_to, message, subject="Happy b-day!"):
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls() # secure connection
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=addr_to, msg=f"Subject:{subject}\n{message}")
            logging.info('Email sent')
    except:
        logging.error('Email was not send')