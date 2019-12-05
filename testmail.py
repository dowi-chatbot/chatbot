import smtplib
from email.mime.text import MIMEText



def envoieMail():
    mail = 'o.dupain@gmail.com'

    message = MIMEText('Ceci est un test !')
    message['Subject'] = 'Test Dowi'

    message['From'] = 'dowidowi930@gmail.com'
    message['To'] = mail

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login('dowidowi930@gmail.com','&dowidowi92!')
        server.send_message(message)
        server.quit()
    except:
        print('L\'adresse du médecin n\‘est pas renseigné')

envoieMail()
