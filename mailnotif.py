
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

account='163'
if account == 'qq':
	host_server = 'smtp.qq.com'
	sender = '814961058@qq.com'
	pwd = 'aoyxasgtwqzzbbja'
elif account == '163':
	host_server = 'smtp.163.com'
	sender = 'jiawenfive@163.com'
	pwd = 'edcyhnvg6mko'

mail_list = ['814961058@qq.com', 'jiawenfive@163.com', 'jiawenfive@yahoo.com']
receivers = sender # mail_list[1] 

mail_title = 'bootcamp program ended'
mail_content = "bootcamp program ended"


smtp = SMTP_SSL(host_server)
smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender, pwd)

msg = MIMEText(mail_content, 'plain', 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender  # Header("python_script", 'utf-8')
msg["To"] = sender #Header("self", 'utf-8')

smtp.sendmail(sender, receivers, msg.as_string())
smtp.quit()
print('email sent')