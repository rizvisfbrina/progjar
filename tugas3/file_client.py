import socket


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = raw_input("Masukkan nama file = ")
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            size = long(data[6:])
            message = raw_input("File tersedia, " + str(size) + "Bytes, download? (y/n)? -> ")
            if message == 'y':
                s.send("OK")
                f = open('new_' + filename, 'wb')
                data = s.recv(1024)
                sizeRecv = len(data)
                f.write(data)
                while sizeRecv < size:
                    data = s.recv(1024)
                    sizeRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((sizeRecv / float(size)) * 100) + "% Done"
                print "Download Selesai!"
                f.close()
        else:
            print "File Tidak Tersedia!"

    s.close()


if __name__ == '__main__':
    Main()