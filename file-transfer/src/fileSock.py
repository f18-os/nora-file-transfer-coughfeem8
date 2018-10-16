import sys, time, threading
sys.path.append('../../empathicDemo')
from framedSock import FramedStreamSock

def _printAnimation():
    ''' prints a small animaiton to chek that the program is still running'''
    sys.stdout.write('0')
    # time.sleep(0.5)
    sys.stdout.write('\b')
    #time.sleep(0.25)
    sys.stdout.write('|')
   #time.sleep(0.5)
    sys.stdout.write('\b')
   # time.sleep(0.25)

def sendFile(filename,sock,*args):
    '''implementation of how to send a file to a server'''
    #t = threading.Thread(target= _printAnimation)
    if args:
        filename = '{}/{}'.format(args[0],filename)
    with open (filename,'rb') as sfile:
        sys.stdout.write('sending data.')
        #t.start()
        while True:
            line = sfile.read(100)
            sock.send(line)
            print(line)
            #t.run()
            _printAnimation()
            if not line: break              
        print()
    sys.stdout.write("data sent.")
    sfile.close()     


'''
def getFile(filename,sock,*args):
 #   implementation of how to get a file from a server 
    #t = threading.Thread(target = _printAnimation)
    if args:
        filename = '{}/{}'.format(args[0],filename)
    with open(filename, 'wb') as rfile:
        sys.stdout.write("recieving data.")
        #t.start()
        while True:
            data = sock.recv(100)
            if not data: break
            rfile.write(data)
            #t.run()
            _printAnimation()
        print()
    rfile.close()
    sys.stdout.write("data recieved")
'''
def getFile(filename,sock,*args):
    '''implementation of how to get a file from a server '''
    #t = threading.Thread(target = _printAnimation)
    if args:
        filename = '{}/{}'.format(args[0],filename)
   # fs = FramedStreamSock(sock, False)
    with open(filename, 'wb') as rfile:
        sys.stdout.write("recieving data.")
        #t.start()
        while True:
            data = sock.recv(100)
            if not data: break
            rfile.write(data)
            #t.run()
            _printAnimation()
        print()
    rfile.close()
    sys.stdout.write("data recieved")
