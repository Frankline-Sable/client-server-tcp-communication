import socket

# Create an INET(ipv4) streaming socket
client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to global webserver on port 9193
client_soc.connect((socket.gethostname(), 9193))

msg = ''
while True:
    temp_msg = client_soc.recv(8)
    msg += temp_msg.decode('utf-8')
    if len(temp_msg) < 8:
        break

print(msg)
