import smtplib
from credentials import e_mail

class send_email_base(object):
    """docstring for send_email_base"""
    def __init__(self, to , subject , text):
        self.to = to
        self.subject = subject
        self.text = text
        self.gmail_user = e_mail['user']
        self.gmail_password = e_mail['password']
        self.sent_from = 'Servidor de Pagina web' 

        

    def send(self):
        email_text = """Subject : {} \n\n {}""".format(self.subject,self.text)
        try:  
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.gmail_user, self.gmail_password)
            server.sendmail(self.sent_from, self.to, email_text)
            server.close()

            print('Email sent!')
        except:  
            print('Something went wrong...')

if __name__ == '__main__':
    a = send_email_base(['luis@4suredesign.com','administracion@borbolla-automation.com'],
                        'Prueba Clase','Texto generico para probar localizacion')

    a.send()
