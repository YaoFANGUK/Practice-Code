# 1. 实现tcp服务器端
# 2. 接收到浏览器发送的http请求报文
# 3. 读取固定页面的数据，构建响应报文并返回
# 4. 关闭客户端的socket


import socket

if __name__ == '__main__':
    # 1. tcp服务器端socket初始化
    # 1.1 create a server socket object
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 1.2 bind a port
    tcp_server_socket.bind(('',9099))
    # 1.3 reuse a port
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, True)
    # 1.4 set listening mode
    tcp_server_socket.listen(128)

    # 1.2 循环接收客户端连接
    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        print(f'Client {ip_port} has connected')
        # 2. 接收到浏览器发送的http请求报文
        recv_data = new_socket.recv(1024)
        if len(recv_data) == 0:
            print('Client has closed the connect')
            new_socket.close()
            continue

        recv_content = recv_data.decode('UTF-8')
        print(recv_content)
        # 3. 读取固定页面的数据，构建响应报文并返回
        #   3.1 读取固定页面的数据
        #   无论什么请求，我都返回一个固定页面 static/index.html
        #       "r":读出字符串数据  "rb":读出二进制数据 (支持读任意文件)
        with open('static/index.html', 'rb') as f:
            file_data = f.read()
        #   3.2 构建响应报文并返回
        # 响应行: HTTP/1.1 200 OK
        # response line
        resonse_line = 'HTTP/1.1 200 OK\r\n'
        # 响应头
        # response header
        resonse_header = 'Server; PWS1.0\r\n'
        # 空行
        # 响应体
        #bilnk line
        resonse_body = file_data
        #   	响应报文：响应行+响应头+空行+响应体
        response_data = (resonse_line + resonse_header + '\r\n').encode('UTF-8') + resonse_body
        # send data
        new_socket.send(response_data)
        # 4. 关闭客户端的socket
        new_socket.close()


