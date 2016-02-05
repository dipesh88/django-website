from .app_settings import TASKS_HOST,TASKS_PORT
from . import worker_manager
from .server import TaskSocketServerThread


worker_manager.start()
server_thread = TaskSocketServerThread(TASKS_HOST,TASKS_PORT)
socket_server = server_thread.socket_server()
socket_server.serve_forever()


