import sys,re,socket, time, os
from threading import Thread
sys.path.append('../test')
sys.path.append('../../emphaticDemo')
import logSetup as log
import params
from framedSock import FramedStreamSock
from fileSock import sendFile, getFile

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

class ServerThread(Thread):
    requestCount = 0            # one instance / class

    def __init__(self, sock, debug,addr):
        Thread.__init__(self, daemon=True)
        self.fsock, self.debug, self.addr = FramedStreamSock(sock, debug), debug, addr
        self.start()

    def run(self):
        fs = FramedStreamSock(sock, debug=debug)
        while True:
            request = self.fsock.receivemsg()
            print("CONNECTION FROM CHILD REC'D FROM ", addr)
            if request:
                request = request.decode('utf-8')
                request = request.rstrip()
            else:
                print( 'SERVER DISCONNECTED FROM {}.'.format(addr))
                break

            #get the client input parsed
            data =  re.split(' ', request)
            try:
                command, f = data
            except:
                print ('WRONG FORMAT RECIEVED')
                continue

            #server sends a file
            if command == 'get':
                if (not os.path.isfile('server/'+f)) or os.stat('server/'+f) <= 0:
                    print('FILE: <{}> NOT IN SERVER/TOO SMALLl.'
                          .format(f))
                    continue
                sendFile(f,sock,'server')
            #server  recieves a file    
            elif command == 'put':
                if os.path.isfile('server/'+f):
                    print('<{}> ALREADY IN SERVER.'.format(f))
                    continue
                getFile(f,sock,'server')
            else:   
                print('WRONG INSTRUCTON RECIEVED.')
                continue
        '''    
            msg = self.fsock.receivemsg()
            if not msg:
                if self.debug: print(self.fsock, "server thread done")
                return
            requestNum = ServerThread.requestCount
            time.sleep(0.001)
            ServerThread.requestCount = requestNum + 1
            msg = ("%s! (%d)" % (msg, requestNum)).encode()
            self.fsock.sendmsg(msg)
        '''

while True:
    sock, addr = lsock.accept() #accept every client that requests
    ServerThread(sock, debug,addr)
