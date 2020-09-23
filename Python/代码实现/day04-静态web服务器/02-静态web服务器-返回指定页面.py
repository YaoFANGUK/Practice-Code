# 1.获取用户请求资源的路径
# 2.根据请求资源的路径，读取指定文件的数据
# 3.组装指定文件数据的响应报文，发送给浏览器
# 4.判断请求的文件在服务端不存在，组装404状态的响应报文，发送给浏览器


import socket

if __name__ == '__main__':
    # 1. tcp服务器端socket初始化
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(('',9099))
    tcp_server_socket.listen(128)

    # 1.2. 循环等待客户端连接
    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        print(f'{ip_port} has connected')

        # 2. 接收到浏览器发送的http请求报文
        recv_data = new_socket.recv(1024)
        # 2.1. 判断浏览器关闭（客户端下线）
        if len(recv_data) == 0:
            print('Client has closed the connection')
            new_socket.close()
            # 跳过当前这次循环
            continue
        recv_str = recv_data.decode()
        # 2.2. 提取请求资源路径
        #   按照空格分割请求报文 (GET /index.html HTTP/1.1\r\n ....)
        #   [0]: GET
        #   [1]: /index.html
        #   [2]: ....
        #   split(分割字符， maxsplit=最大分割次数)
        request_path = recv_str.split('', maxsplit=2)[1]

        # 2.3. 如果没有请求指定页面，那么设置默认首页
        try:
            with open('static' + request_path, 'rb') as f:
                file_data = f.read()
        except Exception as e:
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            with open('static/' + 'errror.html', 'rb') as f:
                file_data = f.read()
        else:
            response_line = 'HTTP/1.1 200 OK\r\n'
        finally:
            # 3. 读取指定页面的数据，构建响应报文并返回
            response_header = 'Server: PWS1.0\r\n'
            response_body = file_data
            response_data = (response_line + response_header + '\r\n').encode('UTF-8') + response_body
            new_socket.send(response_data)
            new_socket.close()
        #   3.1 读取指定页面的数据
        #       无论什么请求，我都返回一个指定页面 static + 请求资源路径
        #       "r":读出字符串数据  "rb":读出二进制数据 (支持读任意文件)



        #   3.2. 请求资源路径，找不到指定文件或者目录


        #   3.3. 请求资源路径，能够找到资源，并返回响应报文




