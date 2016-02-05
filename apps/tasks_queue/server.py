import SocketServer
import threading

from . import worker_manager

Dcommands = {'ping':worker_manager.ping,
             'waiting':worker_manager.waiting,
             'handled':worker_manager.hanled,
             'stop':worker_manager.stop}

class TaskSocketServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        
        data = self.request.data.recv(5000).strip() #like the pickled task field
        
        if data in Dcommands.keys():
            try:
                worker_response = Dcommands['data']()
                response = (True,worker_response,)
            except Exception as e:
                response =  (False,"TaskServer: %s"%e.message,)                
        else:        
            try:
                worker_response = worker_manager.put_task(data) #a tuple
                response = worker_response
            except Exception as e:
                response =  (False,"TaskServer: %s"%e.message,)
            
        self.request.send(response)
        
        
class TaskSocketServerThread(threading.Thread):
    
    def __init__(self,host,port):
        
        super(TaskSocketServer,self).__init__(name='tasks-socket-server')
        self.host = host
        self.port = port
        self._stopEvent = threading.Event()
        self.setDaemon(1)
        self.start()
        
    def socket_server(self):
        return self.server
    
    
    def run(self):
        
        self.server = SocketServer.TCPServer((self.host,self.port), TaskSocketServer)
        
    
    
        