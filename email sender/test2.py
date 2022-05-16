import smtplib
import mimetypes

def main(fromaddress,toaddress,replyto,subject,body,attachment):

    from email.message import EmailMessage

    AUTH_ADDR = "@gmail.com"
    AUTH_PASS = ""

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = fromaddress
    msg['To'] = toaddress
    msg['Reply-to'] = replyto
#    msg['Body'] = body
    msg.set_content(body)

    ctype, encoding = mimetypes.guess_type(attachment)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    with open(attachment, 'rb') as file:
        msg.add_attachment(file.read(),
                               maintype=maintype,
                               subtype=subtype,
                               filename=attachment.split('/')[-1])

    with smtplib.SMTP_SSL('smtp-relay.gmail.com', 465) as smtp:
        smtp.login(AUTH_ADDR, AUTH_PASS)
        smtp.sendmail(fromaddress,toaddress,msg.as_string())

main('jalismahamud2055@gmail.com','jm.tarif55@gmail.com','jalis.tarif55@gmail.com','hi','hello','test.py')