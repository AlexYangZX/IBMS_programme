import socket  # 导入 socket 模块
import time


# 建立连接
def link_start(get_path):
    print('等待客户端连接...')
    s = socket.socket()  # 创建 socket 对象
    host = socket.gethostname()  # 获取本地主机名
    port = 6666  # 设置端口
    s.bind((host, port))  # 绑定端口

    s.listen(5)  # 等待客户端连接

    while True:
        c, addr = s.accept()  # 建立客户端连接
        print('连接成功√')

        while True:
            path = get_path  # 最短路径规划， 结果返回路径节点矩阵

            # 发送消息到Pi
            mes = path
            mes = str(mes).encode()
            c.send(mes)
            # 接收Pi的消息
            n = c.recv(1024)
            n = n.decode()

            if n == 'got it':
                break

        break


def link_restart():
    s = socket.socket()  # 创建 socket 对象
    host = socket.gethostname()  # 获取本地主机名
    port = 6665  # 设置端口
    s.bind((host, port))  # 绑定端口
    s.listen(5)  # 等待客户端连接

    while True:
        c, addr = s.accept()  # 建立客户端连接
        while True:
            # 发送消息到Pi
            mes = 're'
            mes = str(mes).encode()
            c.send(mes)
            # 接收Pi的消息
            n = c.recv(1024)
            n = n.decode()

            if n == 'got it':
                break

        break


def link_shutdown(shut):
    s = socket.socket()  # 创建 socket 对象
    host = socket.gethostname()  # 获取本地主机名
    port = shut  # 设置端口
    s.bind((host, port))  # 绑定端口
    s.listen(5)  # 等待客户端连接

    while True:
        c, addr = s.accept()  # 建立客户端连接
        while True:
            # 发送消息到Pi
            mes = 'shutdown'
            mes = str(mes).encode()
            c.send(mes)
            # 接收Pi的消息
            n = c.recv(1024)
            n = n.decode()

            if n == 'got it':
                break
        s.shutdown()
        break


