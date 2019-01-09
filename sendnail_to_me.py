from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


def sendmail_to_me(title, text):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # 发件人的邮箱
    sender_qq_mail = '569429024@qq.com'
    # pwd为qq邮箱的授权码
    pwd = 'zinddowsyprwbbaa'
    # 收件人邮箱
    receiver = 'liuhao2011@qq.com'
    # 邮件的正文内容
    mail_content = text
    # 邮件标题
    mail_title = title
    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    # smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq_mail, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

