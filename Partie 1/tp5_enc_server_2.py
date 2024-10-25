import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 9998))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        data1 = conn.recv(3)
        if not data1: break
        data2 = conn.recv(3)

        bindata1 = bin(int.from_bytes(data1, byteorder='big'))[2:].zfill(24)
        bindata2 = bin(int.from_bytes(data2, byteorder='big'))[2:].zfill(24)
        opbin = bindata1[0:2]
        sign1 = bindata1[2:3]
        sign2 = bindata1[3:4]
        nb1 = int(bindata1[5:],2)
        nb2 = int(bindata2,2)
        match int(opbin,2) :
            case 0:
                operator = "+"
            case 1:
                operator = "-"
            case 2:
                operator = "*"
            case 3:
                operator = "/"
        if sign1 == bin(0) :
            nb1*-1
        if sign2 == bin(0) :
            nb2*-1
        calcul = str(nb1) + operator + str(nb2)
        result = eval(calcul)
        conn.send(str(result).encode())
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
