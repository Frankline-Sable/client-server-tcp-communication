import socket
import time

HOST = socket.gethostname() # public host visible to the outside world
PORT = 9193 # Port to listen in (non-privileged ports are >1023)
# Create an INET(ipv4) streaming socket
server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a public host, and a custom port
server_soc.bind((HOST, PORT))

# Specifying the maximum connections allowed to the server
max_conn = 5
# Become a server socket
server_soc.listen(max_conn)

# Dict to containing the clients details.
connection_pool = {}
while True:
    status = "resumed" if connection_pool else "started"
    print(f"\n{status} network sniffing")

    client_soc, address = server_soc.accept()
    max_conn -= 1
    print(f"sniffed address {address} remaining {max_conn} connections")

    msg = client_soc.send(
        bytes(f"Hi ip {address[0]} you connected to {socket.gethostname()} on {time.asctime()}", 'utf-8'))
    connection_pool[address] = msg
