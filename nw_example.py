'''
from socket import *

s = socket(AF_INET,SOCK_STREAM)
host = gethostname()
port = 12347
s.bind((host, port))

s.listen(5)
while True:
   c, addr = s.accept()
   print ('Got connection from', addr)
   c.send(b'Thank you for connecting')
   c.close()
'''
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
host = gethostname()
port = 12347
s.bind((host, port))

while True:
    data, addr = s.recvfrom(1000)
    resp = "Get off my lawn!"
    s.sendto(resp, addr)
