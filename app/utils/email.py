"""
Mail to send links and updation key
"""

from app.consts.envs import EMAIL_ID , EMAIL_PWD

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


content = """
    <!DOCTYPE HTML>
    <html>
    <head>
    <meta charset='UTF-8'>
    </head>
    <body>
    <h2>Summaritizer</h2>
    <h3>Here are the details of your new post at Summaritizer</h3>
    <p>Updation Key : {3} </p><br>
    <p>Updation Link : <a href='{0}/update/{1}-{2}'>{0}/update/{1}-{2}</a></p><br>
    <p>Shareable Link : <a href='{0}/view/{1}-{2}'>{0}/view/{1}-{2}</a></p><br>
    <p>Expires After {4} {5}</p>
    </body>
    </html>
"""


def send_email(rec, url, _id, _uuid, key, hrs, mins):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Summaritizer New Post'
    msg['From'] = EMAIL_ID

    smtp = SMTP('smtp.gmail.com' , 587)
    smtp.starttls()

    #Login to email services
    smtp.login(EMAIL_ID, EMAIL_PWD)

    msg['To'] = rec

    hrs_str = "{} hour(s)".format(hrs) if hrs > 0 else ""
    mins_str = "{} minute(s)".format(mins) if mins > 0 else ""

    mail_content = MIMEText(
        content.format(url, _id, _uuid, key, hrs_str, mins_str),
        'html')
    
    msg.attach(mail_content)

    #Send Mail
    smtp.sendmail(EMAIL_ID, rec , msg.as_string())

    print("[ 📧 📬 ] %s" %rec)

    smtp.quit()
