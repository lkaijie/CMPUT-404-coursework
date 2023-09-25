import socket, sys

HOST = "127.0.0.1"
PORT = 8080
buffer_size = 4096
request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"

def get(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(request)
        s.shutdown(socket.SHUT_WR)
        
        data = b""
        
        while True:
            response = s.recv(buffer_size)
            if not response:
                break
            
            data += response
        return data
    
def main():
    response = get(HOST, PORT, request)
    print(response)
        
         


if __name__ == "__main__":
    main()