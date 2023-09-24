import socket, sys



# creating tcp socket
def create_tcp_socket():
    try:
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
    except (socket.error, msg):
        print(str(msg[0]))
        sys.exit()
    print("socket created")
    return s


HOST = "127.0.0.1"
PORT = 8080
buffer_size = 2048
request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"

def get():

    s = create_tcp_socket()    
    s.connect((HOST, PORT))
    s.send(request) # no need to encode because of b (byte) string
    s.shutdown(socket.SHUT_WR)
    
    
    data = b""
    received = True
    while received:
        received = s.recv(buffer_size)
        data += received
        
        return data
    
def main():
    print(get())
    
    
if __name__ == "__main__":
    main()