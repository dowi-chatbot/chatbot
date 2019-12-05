import smtplib

# Specifying the from and to addresses

fromaddr = 'dowidowi930@gmail.com' # A modifier
toaddrs  = 'o.dupain@gmail.com' # A modifier

# Writing the message (this message will appear in the email)

msg = 'Enter you message here' # A modifier

# Gmail Login

username = 'dowidowi930' # A modifier
password = '&dowidowi92!' # A modifier

# Sending the mail  

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()