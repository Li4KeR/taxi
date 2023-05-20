import requests


token = '5811959147:AAHY45MoVaI2c5Qa2hh_IX6_5czKhvknB3E'
url = f"https://api.telegram.org/bot{token}/getUpdates"
my_id = '853337288'


def send_mail(input_from, input_where, input_phone, input_class_taxi):
    # print(requests.get(url).json())
    print(input_from)
    print(input_where)
    print(input_phone)
    print(input_class_taxi)
    message = f'From: {input_from}\nWhere: {input_where}\nPhone: {input_phone}\nTaxi: {input_class_taxi}'
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={my_id}&text={message}"
    print(requests.get(url).json())
    return True
