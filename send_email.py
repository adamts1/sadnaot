import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "kryonps@gmail.com"
receiver_email = "kryonps@gmail.com"
password = "Kryon123!"

SUBJECT = "subject"
TEXT = "text"
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)