import socket

def main():
    host = '0.0.0.0' # '192.168.0.31'
    port = 6000
    addr_server = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket()
    s.bind(addr_server)
    print("Sever Address: ", addr_server)
    s.listen(1)
    
    c, addr_client = s.accept()
    print("Client Address:",str(addr_client))

    while(True):
        data = c.recv(1024).decode()
        if not data:
            break
        print("Received from clinent:", str(data))
        data = '>>> ' + str(data)
        print("Sending to client:", str(data))
        c.send(data.encode())
    c.close()

if __name__ == '__main__':
    main()
