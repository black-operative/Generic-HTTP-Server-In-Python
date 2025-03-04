HTTP_200_OK  = 'HTTP/1.1 200 OK\r\n'
HTTP_404_ERR = 'HTTP/1.1 404 NOT FOUND\r\n'
HTTP_405_ERR = 'HTTP/1.1 405 METHOD NOT ALLOWED\r\n'

CONTENT_HTML = 'text/html'
CONTENT_CSS  = 'text/css'
CONTENT_JS   = 'application/javascript'

class HTTP_Response:
    def __init__(self, header : str, content_type : str, body : str) -> None:
        self.__header__       = header
        self.__content_type__ = content_type
        self.__body__         = body
        self.__body_length__  = len(body)
        
    def generate_headers(self) -> str:
        return (
            f"{self.__header__}"
            f"Content-Type: {self.__content_type__}\r\n"
            f"Content-Length: {self.__body_length__}\r\n"
            "\r\n"
        )
        
    def get_body(self) -> str:
        return self.__body__