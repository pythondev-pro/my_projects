import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'your email'
email['to'] = 'recepient email'
email['subject'] = 'Give thanks!'

email.set_content(html.substitute({'firstname': 'Brother', 'lastname':'Dia '}, home_name='(Dadinho)'), 'html')

with smtplib.SMTP(host='outlook-emeacenter3.office365.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('your email login', 'your email password')
	smtp.send_message(email)
