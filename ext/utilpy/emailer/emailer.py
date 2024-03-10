import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.header import Header

def sendemail(smtp,port,from_email,password,to,subject,content):
    """
    发送邮件
    :param smtp:str smtp服务器,例如smtp.qq.com
    :param port:int 端口
    :param from_email:str 邮箱地址
    :param password:str 邮箱密码,QQ邮箱中则为授权码
    :param to:str 收件邮箱
    :param subject:str 主题
    :param content:str 邮件内容,支持HTML渲染
    
    :return str 成功返回空文本,失败返回原因
    """
    # 连接到SMTP服务器
    con = smtplib.SMTP_SSL(smtp, port)
    try:
        # 登录SMTP服务器
        con.login(from_email,password)
    except smtplib.SMTPAuthenticationError as e:
        return e.args[0]
    except smtplib.SMTPServerDisconnected as e:
        return e.args[0]
    # 创建一个MIMEMultipart对象，用于构建邮件内容
    msg = MIMEMultipart()
    # 设置邮件主题
    subject = Header(subject, 'utf-8').encode() 
    msg['Subject'] = subject
    # 设置发件人
    msg['From'] = from_email
    # 设置收件人
    msg['To'] = to

    html = MIMEText(content, 'html', 'utf-8') 
    msg.attach(html)
    try:
        # 发送邮件
        con.sendmail(from_email ,to, msg.as_string()) 
        con.quit()
        return ""
    except smtplib.SMTPException as e:
        con.quit()
        return e.args[0]

class Emailer:
    """
    邮件发送器,将发送邮件封装到一个类中,避免多次连接服务器
    """
    def __init__(self,smtp,port,from_email,password):
        """
        :param smtp:str smtp服务器,例如smtp.qq.com
        :param port:int 端口
        :param from:str 邮箱地址
        :param password:str 邮箱密码,QQ邮箱中则为授权码
        """
        # 连接到SMTP服务器
        self.con = smtplib.SMTP_SSL(smtp, port)
        self.from_email = from_email
        try:
            # 登录SMTP服务器
            self.con.login(from_email,password)
        except smtplib.SMTPAuthenticationError as e:
            raise Exception("Connect to the smtp server failed.")
        except smtplib.SMTPServerDisconnected as e:
            raise Exception("Connect to the smtp server failed.")
    def sendemail(self,to,subject,content):
        """
            发送邮件
        :param to:str 收件邮箱
        :param subject:str 主题
        :param content:str 邮件内容,支持HTML渲染
        
        :return str 成功返回空文本,失败返回原因
        """
        msg = MIMEMultipart()
        # 设置邮件主题
        subject = Header(subject, 'utf-8').encode() 
        msg['Subject'] = subject
        # 设置发件人
        msg['From'] = self.from_email
        # 设置收件人
        msg['To'] = to

        html = MIMEText(content, 'html', 'utf-8') 
        msg.attach(html)
        try:
            # 发送邮件
            self.con.sendmail(self.from_email ,to, msg.as_string())
            return ""
        except smtplib.SMTPException as e:
            return e.args[0]
