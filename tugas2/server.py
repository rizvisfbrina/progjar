import socket
import os
from threading import Thread

HOST = "127.0.0.1"
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

imgname = ["dotty.png", "marshal.png", "punchy.png"]

def sendImage(ip_client, port_client):
    addr = (ip_client, port_client)
    server_socket.sendto("START", (addr))

    for i in imgname:
        size = os.stat(i).st_size
        server_socket.sendto("SEND {}".format(i), (addr))

        myfile = open(i, 'rb')
        bytes = myfile.read()
        sentSize = 0

        for x in bytes:
            server_socket.sendto(x, (addr))
            sentSize = sentSize + 1
            print "\r sent {} of {} ".format(sentSize, size)

        server_socket.sendto("FINISH",(addr))
        myfile.close()
    server_socket.sendto("END", (addr))

while True:
    data, addr = server_socket.recvfrom(1024)
    print "Receiving: " + str(data)
    if str(data) == "READY":
        thread = Thread(target=sendImage, args=(addr))
        thread.start()
