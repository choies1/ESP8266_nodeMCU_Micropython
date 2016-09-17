# -*- coding: utf-8 -*-
"""
Title: TCP/IP Networing Test (Client)
Author: Eunseok Choi
Date: 2016-09-17
"""
import socket

def Main():
    # host = '127.0.0.1'
    # port = 5000

    host = '192.168.0.31' #'0.0.0.0'
    port = 6000

    s = socket.socket()
    s.connect((host,port))

    message = input("-->")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print("Received from server: ", str(data))
        message = input("-->")
    s.close()

if __name__ == '__main__':
    Main()
