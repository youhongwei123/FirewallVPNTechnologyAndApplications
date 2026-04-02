import socket

SERVER_IP = '8.137.86.107'   # 从黑板上抄
PORT = 31317

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

# 发送自己的名字
client.send('我是刘娜'.encode())

# 接收服务器回应
data = client.recv(1024)
print('服务器说：', data.decode())

client.close()