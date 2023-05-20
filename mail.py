import requests
import sqlite3
from datetime import datetime


token = '5811959147:AAHY45MoVaI2c5Qa2hh_IX6_5czKhvknB3E'
url = f"https://api.telegram.org/bot{token}/getUpdates"
my_id = '-1001827546469'
# my_id = '853337288'


def test():
    url_test = f"https://api.telegram.org/bot{token}/getUpdates"
    print(requests.get(url_test).json())


def check_sql():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS sales(
                id INTEGER PRIMARY KEY,
                in_from TEXT NOT NULL,
                in_where TEXT NOT NULL,
                phone TEXT NOT NULL,
                class_taxi TEXT NOT NULL,
                date_create TEXT);
                """)

    conn.commit()
    cursor.close()


def add_sql(input_from, input_where, input_phone, input_class_taxi):
    date = datetime.now()
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute(f"""
            INSERT INTO sales(in_from, in_where, phone, class_taxi, date_create) 
            VALUES('{input_from}', '{input_where}', '{input_phone}', '{input_class_taxi}', '{date}')""")
    conn.commit()
    cursor.close()


def send_mail(input_from, input_where, input_phone, input_class_taxi):
    check_data = (input_from, input_where, input_phone, input_class_taxi)
    for item in check_data:
        if item == '':
            return False
        else:
            continue
    message = f'Откуда: {input_from}\nКуда: {input_where}\nТелефон: {input_phone}\nКласс: {input_class_taxi}'
    url_link = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={my_id}&text={message}"
    requests.get(url_link).json()
    check_sql()
    add_sql(input_from, input_where, input_phone, input_class_taxi)
    return True
