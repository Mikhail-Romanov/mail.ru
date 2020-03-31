#связывание с сервером c mail.ru

#import imaplib
#import email 

#mail = imaplib.IMAP4_SSL('imap.mail.ru')
#mail.login('es.ee.13@mail.ru', 'essloas31')
#mail.list()
#mail.select("inbox")
#print(mail.list())

#отпрвка писем 

import smtplib 

log = 'es.ee.13@mail.ru'
pas = 'essloas31'
ser = 'smtp.mail.ru'
port = '465'

serv = smtplib.SMTP_SSL(ser, port)
serv.login(log,pas)

sud = 'test'
to = 'es.ee.13@mail.ru'
from_ = 'es.ee.13@mail.ru'
msg_txt = 'text'

do = '\r\n'.join(
	('From: %s' % from_,
	'to: %s' % to,
	'sud: %s' % sud,
msg_txt))
serv.sendmail(from_, [to], do)

print('Успeшно')



#import imaplib
#mail = imaplib.IMAP4_SSL('imap.mail.com', 993)
#mail.login('es.ee.13@mail', 'essloas31')
#mail.list()
#mail.select("inbox")

#
#ser = 'pop.gmail.com'
#port = '995'

#log = 'alsy.love.you@gmail.com'

#passw = 'alsy.love.you'
#box = poplid.POP_SSL(STARTTLS,587)

#box.user(log)
#box.pass_(passw)
#box.list()
#print(box.list())