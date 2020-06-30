from flask import Flask, render_template, request, redirect, url_for
import smtplib, ssl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.jinja2')


@app.route('/test', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # result = request.form
        application_name = request.form.get('name')
        application_subject = request.form.get('subject')
        application_message = request.form.get('message')
        application_email = request.form.get('email')
        subject = "פניה מאתר סדנאות"
        TEXT = " שם: "+application_name+"\n"+" נושא: "+application_subject+"\n"+" פרטי הודעה: "+application_message+"\n"+" דואר אלקטרוני: "+application_email
        message = 'Subject: {}\n\n{}'.format(subject, TEXT).encode('utf-8')
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "kryonps@gmail.com"
        receiver_email = "kryonps@gmail.com"
        password = "Kryon123!"

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return render_template('home.jinja2')



if __name__ == '__main__':
    app.run(debug=True)
