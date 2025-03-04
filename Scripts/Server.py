import socket
import sys
import os
import mimetypes
import File
import HTTP

PORT        = 3000
LOCAL_HOST  = '127.0.0.1'
BUFFER_SIZE = 66536
WEB_DIR     = os.path.abspath(os.path.join(os.path.dirname(__file__), '../web'))

class HTTP_Server:
    def __init__(self):
        self.Server_Socket  = None
        self.Server_Address = (LOCAL_HOST, PORT)
        self.Client_Socket  = None
        self.Client_Address = None
        self.Response       = None
        self.File_Content   = File.File_Reader()

    def init_server(self) -> None:
        try:
            self.Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.Server_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.Server_Socket.bind(self.Server_Address)
            self.Server_Socket.listen(10)
            print(f"Server started on port: {PORT}")

        except socket.error as err:
            print("Failed to start server. Error:", err)
            sys.exit()

    def accept_connections(self) -> None:
        try:
            while True:
                self.Client_Socket, self.Client_Address = self.Server_Socket.accept()
                print("Client connected from:", self.Client_Address)
                self.handle_client_request()

        except KeyboardInterrupt:
            self.stop_server()
        
        except socket.error as err:
            print("Error accepting connection:", err)
            self.stop_server()

    def handle_client_request(self) -> None:
        try:
            request = self.Client_Socket.recv(BUFFER_SIZE).decode('utf-8')
            if not request:
                print("Client disconnected")
                return
            print("Received request:", request)
            
            request_line = request.split('\r\n')[0]
            request_parts = request_line.split(' ')
            method, path = request_parts[0], request_parts[1]
            
            if method != 'GET':
                self.illegal_method_response()
                return
            
            file_path = os.path.join(WEB_DIR, path.lstrip('/'))

            if os.path.isdir(file_path):
                file_path = os.path.join(file_path, 'index.html')
            
            if os.path.exists(file_path) and os.path.isfile(file_path):
                self.File_Content.set_file_path(file_path)
                content_type = mimetypes.guess_type(file_path)[0] or 'application/octet-stream'
                content = self.File_Content.read_file()
                self.Response = HTTP.HTTP_Response(HTTP.HTTP_200_OK, content_type, content)
                self.send_file_response()
            else:
                self.not_found_response()

        except KeyboardInterrupt:
            self.stop_server()
        
        except socket.error as err:
            print("Error handling request:", err)
            self.stop_server()

    def send_file_response(self) -> None:
        headers       = self.Response.generate_headers()
        body          = self.Response.get_body()
        full_response = (headers + body).encode('utf-8')
        self.Client_Socket.sendall(full_response)
    
    def illegal_method_response(self) -> None:
        self.Response = HTTP.HTTP_Response(
            HTTP.HTTP_405_ERR,
            HTTP.CONTENT_HTML,
            '<!DOCTYPE html><html lang="en"><head></head><body><h1>405 METHOD NOT ALLOWED</h1></body></html>'
        )
        self.send_file_response()
    
    def not_found_response(self) -> None:
        self.Response = HTTP.HTTP_Response(
            HTTP.HTTP_404_ERR,
            HTTP.CONTENT_HTML,
            '<!DOCTYPE html><html lang="en"><head></head><body><h1>404 NOT FOUND</h1></body></html>'
        )
        self.send_file_response()
    
    def stop_server(self) -> None:
        print("\nShutting Down...")    
        try:
            if self.Server_Socket:
                self.Server_Socket.close()

            if self.Client_Socket:
                self.Client_Socket.close()

        except Exception as err:
            print("Error stopping server:", err)
        
        finally:
            print("Server stopped")
            sys.exit()