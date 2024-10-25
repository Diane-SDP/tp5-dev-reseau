import re
import socket

def validate_input(message):
    pattern = r'^(-?\d{1,6})\s*([+\-\/*])\s*(-?\d{1,6})$'
    match = re.match(pattern, message)
    if match:
        num1, operator, num2 = int(match.group(1)), match.group(2), int(match.group(3))
        if -1048575 <= num1 <= 1048575  and -1048575  <= num2 <= 1048575 :
            return True
    return False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

msg = input("Calcul : ")
while not validate_input(msg) :
    msg = input("Mauvais input chien : ")

encoded_msg = msg.encode('utf-8')
msg_len = len(encoded_msg)
header = msg_len.to_bytes(4, byteorder='big')
ending_seq = "<clafin>".encode('utf-8')
s.send(header + encoded_msg + ending_seq)

s_data = s.recv(1024)
print(s_data.decode())


s.close()
