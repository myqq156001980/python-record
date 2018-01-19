import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

mailto_list = ['***@lianjia.com']
mail_host = "smtp.163.com"  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 口令
mail_postfix = "163.com"  # 发件箱的后缀


def send_mail(to_list, sub):
    def addimg(src, imgid):  # 文件路径、图片id
        fp = open(src, 'rb')  # 打开文件
        msgImage = MIMEImage(fp.read())  # 读入 msgImage 中
        fp.close()  # 关闭文件
        msgImage.add_header('Content-ID', imgid)
        return msgImage

    msg = MIMEMultipart('related')
    # HTML代码
    msgtext = MIMEText("""
    <div style="height: 400px"><img src="cid:io"></div>
    <div style="height: 400px"><img src="cid:io"></div>
    <div style="width:50%; height: 400px"><img src="cid:io"></div>
    <div style="width:50%; height: 400px"><img src="cid:io"></div>
    """, "html", "utf-8")
    msg.attach(msgtext)
    msg.attach(addimg("a.jpg", "io"))  # 全文件路径，后者为ID 根据ID在HTML中插入的位置
    msg.attach(addimg("a.jpg", "key_hit"))  # 同上
    msg.attach(addimg("a.jpg", "men"))  # 同上
    msg.attach(addimg("a.jpg", "swap"))  # 同上
    me = "163" + "<" + mail_user + "@" + mail_postfix + ">"
    msg['Subject'] = sub  # 主题
    msg['From'] = me  # 发件人
    msg['To'] = ";".join(to_list)  # 收件人列表
    try:
        server = smtplib.SMTP()  # SMTP
        server.connect(mail_host)  # 连接
        server.login(mail_user, mail_pass)  # 登录
        server.sendmail(me, to_list, msg.as_string())  # 发送邮件
        server.close()  # 关闭
        return True
    except Exception as e:
        print(str(e))
        return False


if __name__ == '__main__':
    if send_mail(mailto_list, "hello"):
        print("发送成功")
    else:
        print("发送失败")
