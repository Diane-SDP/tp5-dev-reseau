import re
import socket 

def validate_input(message):
    pattern = r'^(-?\d{1,6})\s*([+\-\/*])\s*(-?\d{1,6})$'
    match = re.match(pattern, message)
    if match:
        num1, operator, num2 = int(match.group(1)), match.group(2), int(match.group(3))
        if -1048575 <= num1 <= 1048575  and -1048575  <= num2 <= 1048575 :
            return True, [num1, operator, num2]
    return False, []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9998))

msg = input("Calcul : ")
checked, listcalcul = validate_input(msg)
while not checked :
    msg = input("Mauvais input chien : ")
    checked, listcalcul = validate_input(msg)
firstnb, operator, secondnb = listcalcul[0],listcalcul[1],listcalcul[2]

match operator :
    case "+" :
        opbin = 0
    case "-" :
        opbin = 1
    case "*" :
        opbin = 2
    case "/" :
        opbin = 3

firstsign = 0
secondsign = 0

if firstnb < 0 :
    firstsign = 1
if secondnb < 0 :
    secondsign = 1

opshift = opbin << 22
firstsignshift = firstsign << 21
secondsignshift = secondsign << 20
firstoctet = opshift | firstsignshift | secondsignshift | int(firstnb)
secondoctet = int(secondnb)
payload = firstoctet.to_bytes(3, byteorder='big') + secondoctet.to_bytes(3, byteorder='big')
s.send(payload)
s_data = s.recv(1024)
print(s_data.decode())
s.close()
