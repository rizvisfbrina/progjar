import socket

HOST = "127.0.0.1"
PORT = 9000
BLOCK_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (HOST, PORT)
sock.sendto("READY", server_address)

def getImage():
    received = 0
    while True:
        data, addr = sock.recvfrom(1024)
        if data[:4] == "SEND":
            print data[5:]
            fp = open(data[5:], "wb+")

        elif data[:6] == "FINISH":
            fp.close()
            received = 0

        elif data[:3] == "END":
            print "END CONNECTION"
            break
        else:
            fp.write(data)
            received += len(data)
            print "Received " + str(received)

while True:
    data, addr = sock.recvfrom(1024)
    if str(data).startswith("START"):
        tmp = str(data).split()
        # print "Got Size"
        getImage()
        break