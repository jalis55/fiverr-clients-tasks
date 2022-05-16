import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from os.path import basename
from email.mime.application import MIMEApplication


def main(fromaddress,toaddress,replyto,subject,body,attachment):


    AUTH_ADDR = "@gmail.com"
    AUTH_PASS = ""

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = fromaddress
    msg['To'] = toaddress
    msg['Reply-to'] = replyto
#    msg['Body'] = body
    # msg.set_content(body)
    msg.attach(MIMEText(body))

    with open(attachment, "rb") as file:
         part = MIMEApplication(
            file.read(),
            Name=basename(attachment)
            )
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(attachment)
    msg.attach(part)


    with smtplib.SMTP_SSL('smtp-relay.gmail.com', 465) as smtp:
        smtp.login(AUTH_ADDR, AUTH_PASS)
        smtp.sendmail(fromaddress,toaddress,msg.as_string())
        