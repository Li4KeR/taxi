from flask import Flask, render_template, url_for, request, redirect
from mail import send_mail


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        input_from = request.form['from']
        input_where = request.form['where']
        input_phone = request.form['phone']
        input_class_taxi = request.form['class_taxi']
        # send_mail(input_from, input_where, input_phone, input_class_taxi)
        print(True)
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
