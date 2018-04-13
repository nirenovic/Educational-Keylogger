import smtplib

class Emailer(object):
    def __init__(self, user, password, recipient, content):
        self.user = user
        self.password = password
        self.recipient = recipient
        self.content = content

    def send_email(self):
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(self.user, self.password)
        mail.sendmail(self.user, self.recipient, self.content)
        mail.close()
