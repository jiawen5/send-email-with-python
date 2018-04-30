
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

host_server = 'smtp.163.com' #smtp.qq.com works too
sender = 'xxx@163.com'
authcode = 'xxx'
# theoretically, it's viable to send to other email accounts
# but it's likely to be intercepted by spam filters
# only sending to yourself is always okay
receivers = sender

mail_title = 'send email with python'
mail_content = "send email with python"

smtp = SMTP_SSL(host_server)
smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender, authcode)

msg = MIMEText(mail_content, 'plain', 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender  # Header("test email", 'utf-8')
msg["To"] = sender #Header("test email", 'utf-8')

smtp.sendmail(sender, receivers, msg.as_string())
smtp.quit()
print('email sent')
