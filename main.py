#=====================#
# Tugas Besar Jarkom  #
#     Kelompok 4      #
#=====================#
# Alifya Difa Afasyah       (1303210019)
# Iqbal Andhika Dharmastyo  (1303210162)
# Moh Rassel Pramadansyah   (1303210019)

# Import modul/library socket dan sys untuk menutup program
from socket import *
import sys

# Menentukan socket ke alamat dan port yang telah ditentukan yang akan diakses melalui web browser
server_host = 'localhost'
port = 8082

# Membuat TCP socket untuk menerima permintaan melalui address dan port yang ditentukan
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_host, port))
server_socket.listen(1)

# Coloring untuk output terminal
default     = '\033[94m'
success     = '\033[92m'
error       = '\033[91m'

print("======================\n\nWeb Server Kelompok 4\n\n======================")
print(f"""
{default}Port Established!

Host: {success}{server_host}
{default}Port: {success}{port}
{default}URL: {success}{server_host}:{port}{default}
====================
""")

while True:
    print(f"{success}Ready to serve...{default}")

    # Menerima permintaan TCP melalui soket yang telah dibangun
    connectionSocket, address = server_socket.accept()

    try:
        # Menerima data dari soket dengan jumlah byte maksimum 1024
        message = connectionSocket.recv(1024)
        filename = str(message.split()[1])

        # Mengirim respon kepada klien berdasarkan permintaan resourcenya
        if filename == "b'/'" or filename == "b'/index.html'":
            filename = 'index.html'
        f = open(filename)
        outputdata = f.read()

        # Mengirim respon header HTTP 200 dan file HTML sesuai permintaan routenya
        http_ok_response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + outputdata
        connectionSocket.send(http_ok_response.encode())
        
        # Menutup koneksi setelah program merespon permintaan klien
        connectionSocket.close()
    except IOError:
        # Jika file atau route tidak ditemukan, respon HTTP 404 Not Found akan dikirim
        filename = '404.html'
        f = open(filename)
        outputdata = f.read()

        not_found_response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n" + outputdata
        connectionSocket.send(not_found_response.encode())

    # Menutup koneksi setelah program merespon permintaan klien
    connectionSocket.close()

# Mengakhiri program dan koneksi TCP apabila program dihentikan
server_socket.close()
sys.exit()
