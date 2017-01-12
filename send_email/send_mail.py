def send_mail(attachment_name):
    smtp_user = 'user'
    smtp_passwd = 'password'
    sender = 'sender@xxxx.com'
    receivers = ['receivers@xxxx.com']

    smtp = smtplib.SMTP('server_address', port)
    smtp.starttls()
    smtp.login(smtp_user, smtp_passwd)

    message = MIMEMultipart()
    message['Subject'] = Header("api-offer rpc statis", 'utf-8')
    ctype, encoding = mimetypes.guess_type(attachment_name)
    maintype, subtype = ctype.split('/', 1)
    with open(attachment_name, 'rb') as fp:
        msg = MIMEBase(maintype, subtype)
        msg.set_payload(fp.read())

    encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment', filename=attachment_name)
    message.attach(msg)
    composed = message.as_string()
    smtp.sendmail(sender, receivers, composed)
    
   if __name__ == '__main__':
      send_mail("your_attachment_name")
