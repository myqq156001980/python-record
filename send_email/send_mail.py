import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import mimetypes
from email.mime.base import MIMEBase
from email import encoders
import os

def send_mail(attachment_name):
    smtp_user = 'user'
    smtp_passwd = 'password'
    sender = 'sender@xxxx.com'
    receivers = ['receivers@xxxx.com']

    message = MIMEMultipart()
    message['Subject'] = Header("api-offer rpc statis", 'utf-8')
    message['From'] = sender
    message['To'] = ','.join(receivers)
    
     # 添加邮件正文内容
    message.attach(MIMEText("the data is in the attachment", 'plain', 'utf-8'))
    
    # 添加邮件附件
    ctype, encoding = mimetypes.guess_type(attachment_name)
    maintype, subtype = ctype.split('/', 1)
    with open(attachment_name, 'rb') as fp:
        msg = MIMEBase(maintype, subtype)
        msg.set_payload(fp.read())
    encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment', filename=os.path.split(attachment_name)[1])
    message.attach(msg)
    
    composed = message.as_string()
    
    smtp = smtplib.SMTP('server_address', port)
    smtp.starttls()
    smtp.login(smtp_user, smtp_passwd)
    smtp.sendmail(sender, receivers, composed)
    
   if __name__ == '__main__':
      send_mail("your_attachment_name")
