import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80))

# 인코딩된 문자열을 변수에 저장
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mySock.send(cmd)    # 저장된 문자열을 소켓을 통해 전송

while True:
    data = mySock.recv(512) # 서버에서 받은 데이터를 변수에 저장
    if(len(data) < 1):
        break

    print(data.decode(),end='') # 출력시 디코딩을 통한 출력

mySock.close()
