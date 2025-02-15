from email.message import EmailMessage
import smtplib, ssl
def email():
    towho = input("To who? ")
    letter = 'Your account has been created. Username: User, Pass: 1234'
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'testmailfortthk@gmail.com'
    #####https://myaccount.google.com/apppasswords
    password = 'esmd plst aeln ydln'
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(letter)
    msg['Subject'] = 'e-mail sending'
    msg['From'] = sender_email
    msg['To'] = towho
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print('Sent')
    except Exception as e:
        print('Error:', e)
email()