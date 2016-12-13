# -*- coding:utf-8 -*-

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib
import traceback
from base64 import b64encode


class Email:
    '''
    发送附件邮件
    '''

    def __init__(self):
        pass

    def sendHtmlEamil(self, server, fro, to, cc, subject, html):

        # 发送Html报告
        msg = MIMEMultipart('related')
        msg['From'] = fro
        msg['Subject'] = '=?%s?B?%s?=' % ('utf-8', b64encode(subject))
        msg['To'] = ','.join(to)
        msg['Cc'] = cc
        msg['Date'] = formatdate(localtime=True)

        msg.preamble = 'This is a multi-part message in MIME format.'
        msgAlternative = MIMEMultipart('alternative')
        msg.attach(msgAlternative)

        # Set HTML MSG
        msgHtml = MIMEText(open(html, 'rb').read(), 'html', 'utf-8')
        msgAlternative.attach(msgHtml)
        self.send(server, fro, to, msg)

    def send(self, server, fro, to, msg):

        # 发送协议
        try:
            # QQ应该用SMTP_SSL加密协议
            smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
            smtp.ehlo()
            smtp.ehlo()
            smtp.login(server.get('user'), server.get('passwd'))
            smtp.sendmail(fro, to, msg.as_string())
            smtp.close()
        except Exception as e:
            print(traceback.format_exc())

    def sendEmail(self, attachfile):

        print("Begin to send email !")
        # 尝试发送邮件， passwd是qq开通SMTP_SSL的权限码
        try:

            server = {'name': 'mail.qq.com', 'port': 465, 'user': '3434633002@qq.com', 'passwd': 'cqwrawjfhiyrcigg',}
            fro = "3434633002@qq.com"
            cc = ["960292235@qq.com"]
            to = ["960292235@qq.com"]
            subject = "ManBoker每日检查报告"

            self.sendHtmlEamil(server, fro, to, cc, subject, attachfile)

        except:
            print "发送报告失败"

        print("End to send email !")


if __name__ == "__main__":
    se = Email()
    se.sendEmail(os.getcwd() + "\\report.html")