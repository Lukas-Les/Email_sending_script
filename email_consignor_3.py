import os
import smtplib
from email.message import EmailMessage
import imghdr


EMAIL_ADDRESS = os.environ.get('lukas_email')
EMAIL_PASS = os.environ.get('lukas_pass')

receivers = ['egzample_receiver@gmail.com']
for receiver in receivers:
	msg = EmailMessage()
	msg['Subject'] = 'Look at me!'
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = receiver
	msg.set_content('This is message text!')

	msg.add_alternative("""\
		<!DOCTYPE html>
		<html>
		    <body>
		        <h1 style="color:SlateGray;">This is message text, but in html!</h1>
		    </body>
		</html>
		""", subtype = 'html')

	with open('./Resources/smiley.jpg', 'rb') as f:
		file_data = f.read()
		file_type = imghdr.what(f.name)
		file_name = f.name

	msg.add_attachment(file_data,
		maintype = 'image',
		subtype = file_type,
		filename = file_name
		)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

		smtp.send_message(msg)