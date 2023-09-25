#!/usr/bin/env python3
import socket
import time
from threading import Thread

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def handle_connection(conn, addr):
    with conn:
        data = b""
        print(f"connected via {addr}")
        
        while True:
            received = conn.recv(BUFFER_SIZE)
            if not received:
                break
            data += received
        conn.sendall(data)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            
            
            # # print(s.accept()) # this will break when i add it fomr some reason(not echoed back)
            # print("Connected by", addr)
            # print("Connected by", conn)
            
            # #recieve data, wait a bit, then send it back
            # full_data = conn.recv(BUFFER_SIZE)
            # time.sleep(0.5)
            # print(full_data)
            # conn.sendall(full_data)
            # conn.close()
            
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()
            

if __name__ == "__main__":
    main()
