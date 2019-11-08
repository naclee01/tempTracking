import os, smtplib

# set email address and password for email account
email = 'email@address.com'
password = 'password'

# query for cpu temp and translate to farenheit
temp = float(os.popen('vcgencmd measure_temp').readline().strip().replace('temp=','').replace("'C",""))
temp = temp * 1.8 + 32

# set variables for email address, recipient, subject, and email body
sent_from = email
sent_to = 'recipient@address.com'
subject = 'Raspberry Pi - Current Temp'
body = 'Currently {0} F.'.format(temp)

# build email
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, sent_to, subject, body)

# try sending email
try:
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(email, password)
	server.sendmail(sent_from, sent_to, email_text)
	server.close()

	# print message if sent
	print ('Email sent!')
except:
	# print message if not sent
	print ('Error - email not sent')
