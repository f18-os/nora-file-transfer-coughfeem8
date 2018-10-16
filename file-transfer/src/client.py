import sys, socket, re, os 
sys.path.append('../test')
import logSetup as log                              # my loggin module
sys.path.append('../../emphaticDemo')
import params
from framedSock import FramedStreamSock
from fileSock import sendFile, getFile
from threading import Thread
import time
switchesVarDefaults = (
    (('-s', '--server'), 'server', "localhost:50000"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug  = paramMap["server"], paramMap["usage"], paramMap["debug"]

if usage:
    params.usage()


try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

class ClientThread(Thread):
    def __init__(self, serverHost, serverPort, debug):
        Thread.__init__(self, daemon=False)
        self.serverHost, self.serverPort, self.debug = serverHost, serverPort, debug
        self.start()
    def run(self):
       #check for the type of conenciton to the server
       while True:
           conn_type = input('what to connect directy to the server? [Y/N]\n')

           # connect coorecty depending on type
           if conn_type.upper() == 'Y':
               serverPort = 50001  #server
               break
           elif conn_type.upper() == 'N': 
               break     #no need to re set the same value
           else:
               print ('WRONG INPUT. TRY AGAIN')
        
       #attempt to connect
       s = None
       for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
           af, socktype, proto, canonname, sa = res
           try:
               print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
               s = socket.socket(af, socktype, proto)
           except socket.error as msg:
               print(" error: %s" % msg)
               s = None
               continue
           try:
               print(" attempting to connect to %s" % repr(sa))
               s.connect(sa)
           except socket.error as msg:
               print(" error: %s" % msg)
               s.close()
               s = None
               continue
           break
       
       if s is None:
           print('could not open socket')
           sys.exit(1)

       

       fs = FramedStreamSock(s, debug=debug)
       #file transfer ================================
       request = input('>>')
       #end command disconecting
       if request == 'exit':
           print('disconecting')
           s.close()
           sys.exit(1)
       else:
            fs.sendmsg(request.encode())

        #check if client uses direct conection to  the server
       data =  re.split(' ', request)
       try:
           command , f = data
       except:
           print ('WRONG NUMBER OF COMMANDS CLOSING CONNECTION')
           sys.exit(1)
       if command == 'put':
           if (not os.path.isfile(f)) or  os.path.getsize(f) == 0:
               print('file: {} doesn\'t exits or is too small.'.format(f))
           else:
               sendFile(f,s)  
       elif command == 'get':
           if os.path.isfile(f):
               print('you already have {}.'.format(f))
           else:
               getFile(f,s)
       else: #zero size command
           print('that\'s  not a good format')

ClientThread(serverHost, serverPort, debug)
