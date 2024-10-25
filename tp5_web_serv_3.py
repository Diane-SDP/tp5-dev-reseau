import socket

host = 'localhost' 
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  

s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

while True : 
    try:
        data = conn.recv(1024)

        if not data: break
        request, url = str(data).split(" ")[0][2:], str(data).split(" ")[1]
        print(f"Réponse du client : {request, url}")

        if request == 'GET':
            if url == '/' :
                conn.sendall(b"HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>")
                break
            if url == '/index':
                file = open('index.html')
                html_content = file.read()
                file.close()
                http_response = 'HTTP/1.0 200 OK\n\n' + html_content
                conn.send(http_response.encode())
                break


    except socket.error:
        print("Error occured")
        break


conn.close()

