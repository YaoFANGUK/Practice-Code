"""This document serves as a client server"""

import socket


def client_request_func(client_socket):
    while True:
        send_str = input('Please enter something:')
        if send_str.lower() == 'bye':
            client_socket.close()
            break
        client_socket.send(send_str.encode('utf-8'))
        print(client_socket.recv(1024).decode('utf-8'))



if __name__ == '__main__':
    # 1. create a socket object
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. connect to the server
    tcp_client_socket.connect(('192.168.43.119',9899))
    # 3. call a request func
    client_request_func(tcp_client_socket)