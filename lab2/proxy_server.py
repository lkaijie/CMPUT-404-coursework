import socket
from threading import Thread


SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080
BYTES_TO_READ = 4096


HOST = "www.google.com"
PORT = 80

def send_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request)
        s.shutdown(socket.SHUT_WR)
        
        response = b""
        
        while True:
            received = s.recv(BYTES_TO_READ)
            if not received:
                break
            
            response += received
        return response
    
    pass


def handle_connection(conn, addr):
    with conn:
        # get info and send request
        # received = conn.recv(BYTES_TO_READ)
        data = b""
        
        while True:
            received = conn.recv(BYTES_TO_READ)
            
            if not received:
                break
            data += received
        
        response = send_request(data)
        conn.sendall(response)
        
        
    
    
    
    pass
    


def start_server():
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((SERVER_IP, SERVER_PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2)
        
        connection, address = s.accept()
        handle_connection(connection, address)
        
def start_threaded_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((SERVER_IP, SERVER_PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2)
        
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()  
        


def main():
    # start_server()
    start_threaded_server()
    
    
if __name__ == "__main__":
    main()