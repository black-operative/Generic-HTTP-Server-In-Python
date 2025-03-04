from Server import HTTP_Server

s = HTTP_Server()
s.init_server()
s.accept_connections()
s.stop_server()