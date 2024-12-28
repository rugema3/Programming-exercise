from flask import Flask, render_template, request
import send_sms

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sms.html')

@app.route('/send', methods= ['POST'])
def send_message():
    sender = request.form['sender']
    phone = request.form['number']
    message = request.form['message']
    send_sms.send_sms(message, sender, phone)
    return None


if __name__ == '__main__':
    app.run(debug=True)
