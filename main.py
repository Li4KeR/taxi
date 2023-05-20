from flask import Flask, render_template, url_for, request, redirect
from mail import send_mail, test


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        # print(request.form['btn_send_form'])
        # if request.form['btn_send_form'] == 'Geo':
        #     print('geo')
        # else:
        input_from = request.form['from']
        input_where = request.form['where']
        input_phone = request.form['phone']
        input_class_taxi = request.form['class_taxi']
        print(input_from)
        if send_mail(input_from, input_where, input_phone, input_class_taxi):
            msg = 'Заказ передан оператору'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Заполните все данные'
            return render_template('index.html', msg=msg)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
