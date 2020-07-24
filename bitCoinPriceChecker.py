import requests
import json
import smtplib

def send_mail(price):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	email = ''

	server.login(email, 'srvsyenmwrjqkiod')

	subject = 'Price fell down!'
	body = 'check it now'

	msg = f"subject: {subject}\n\n{body, price}"

	server.sendmail(
		email,
		email,
		msg
	)
	print("email has been sent")
	server.quit()


#send_mail()
URL = 'https://coincheck.com/api/rate/'

coins = {'XLM': 'xlm_jpy'}

toggle = True

while toggle:
	for key, item in coins.items():
	    coincheck = requests.get(URL+item).json()
	    # print("%-4s : %-10s" % (key, coincheck['rate']))

	    if float(coincheck['rate']) < 10.5:
	    	send_mail(coincheck['rate'])
	    	toggle = False
	    	


