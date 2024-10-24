import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9999))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        header = conn.recv(4)
        if not header: break
        lenght = str(int.from_bytes(header, byteorder='big'))
        lenght = '0' * (4- len(lenght)) + lenght
        calcul = conn.recv(int(lenght)).decode()
        end_seq = conn.recv(8).decode()
        if end_seq != "<clafin>" :
            print("il manque la sequence de fin flute alors")
            break
        print(f'Message du client : {lenght}{calcul}{end_seq}')

        res  = eval(calcul)
        conn.send(str(res).encode())
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
