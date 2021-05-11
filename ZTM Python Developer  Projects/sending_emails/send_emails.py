import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'your email'
email['to'] = 'recepient email'
email['subject'] = 'Give thanks!'
email.set_content('You did it, Brother')

with smtplib.SMTP(host='outlook-emeacenter3.office365.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('your email', 'your email password')
	smtp.send_message(email)
