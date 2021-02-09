import socket

s = socket.socket()
host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024))
s.close

'''
from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("www.google.com",80))
s.send(b"GET /index.html HTTP/1.0\n\n") 
data = s.recv(10000) # Get response
print(data)
s.close()


import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login("sender_email_id", "sender_email_id_password")

message = "Message_you_need_to_send"

s.sendmail("sender_email_id", "receiver_email_id", message)

s.quit()
'''
