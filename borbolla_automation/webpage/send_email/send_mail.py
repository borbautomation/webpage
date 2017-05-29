import smtplib
from credentials import e_mail
gmail_user = e_mail['user']
gmail_password = e_mail['password']

sent_from = gmail_user  
to = ['administracion@borbolla-automation.com', 'lic.myriamdelgado@gmail.com']  
subject = 'OMG Super Important Message'  
body = 'Hey, whats up?\n\n- You'

email_text = """Subject : {} \n\n {}""".format(subject,body)
try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:  
    print('Something went wrong...')
