# Generic HTTP Web Server in Python

## Description

This project is an HTTP Web Server for static webpages using sockets.

<!-- The architecture is similar yet different to other projects in the series of [HTTP Web Servers](#). -->

## Installation

You can use the following methods to clone this repo to your local machine:

1. **HTTP Clone**

    ```bash
    git clone https://github.com/black-operative/Generic-HTTP-Server-In-Python.git
    ```

2. **GitHub Desktop**
    - **File**
        - `Alt + f`
    - **Clone Repository**  
        - `Alt + f` + `n`
        - `Ctrl + Shift + O`
    - **URL Tab**
    - **Repo URL** *or* Username + Repo name:  
        - `https://github.com/black-operative/Generic-HTTP-Server-In-Python.git`
        - `black-operative/Generic-HTTP-Server-In-Python`
    - **Local Path**: Pick any location that you want.

3. **GitHub CLI**

    ```bash
    gh repo clone black-operative/Generic-HTTP-Server-In-Python
    ```

## Code Organization

Code is organized into two directories:

```plaintext
├── Scripts
│   ├── File.py
│   ├── HTTP.py
│   ├── Main.py
│   └── Server.py
└── web
    ├── index.html
    ├── index.js
    └── style.css
```

## Features

- [**OOP**](https://en.wikipedia.org/wiki/Object-oriented_programming) Architecture
- [**Network Socket**](https://en.wikipedia.org/wiki/Network_socket) Architecture
- [**IPv4**](https://en.wikipedia.org/wiki/IPv4) Protocol
- Static Website Hosting
- MIME Type Handling
- Custom Error Handling (404, 405 Responses)

## Modules

### 1. File

This module is responsible for reading a requested file.

#### Member

- `__file_path__`: String containing the path to the requested file.

#### Methods

##### 1. `set_file_path()`

Initializes the `__file_path__` variable.

```python
set_file_path(file_path: str) -> None
```

- **file_path**: Path of the file to be read.
- No return value.

##### 2. `read_file()`

Reads and returns the contents of a file.

```python
read_file() -> str
```

- Returns the content of the file as a string.

### 2. HTTP

This module is responsible for providing the HTTP Response container and useful macros.

#### Macros

```plaintext
CONTENT_HTML  = 'text/html'                           # HTTP Request: Content Type HTML
CONTENT_CSS   = 'text/css'                            # HTTP Request: Content Type CSS
CONTENT_JS    = 'application/javascript'              # HTTP Request: Content Type JavaScript            
HTTP_200_OK   = 'HTTP/1.1 200 OK\r\n'                 # HTTP 200 OK Response Header
HTTP_404_ERR  = 'HTTP/1.1 404 NOT FOUND\r\n'          # HTTP 404 Not Found Response Header                
HTTP_405_ERR  = 'HTTP/1.1 405 METHOD NOT ALLOWED\r\n' # HTTP 405 Method Not Allowed Response                        
```

#### Members

- `__header__`: HTTP Header with status code.
- `__content_type__`: HTTP Response MIME (content) type.
- `__body__`: HTTP Response content to be sent.
- `__body_length__`: Length of the HTTP Response content.

#### Methods

##### 1. `generate_headers()`

Generates the HTTP Response header to be sent.

```python
generate_headers() -> str
```

- Returns an HTTP response header based on the content to be sent and the status of the server or request.

##### 2. `get_body()`

Getter function that returns the content to be sent in an HTTP Response.

```python
get_body() -> str
```

- Returns the `__body__` member variable.

### 3. Server

This module implements the HTTP server using socket programming.

#### Members

- `Server_Socket`: The main server socket.
- `Server_Address`: The server's address and port.
- `Client_Socket`: The socket for communicating with the client.
- `Client_Address`: The client's address.
- `Response`: Stores the HTTP response object.
- `File_Content`: Instance of `File_Reader` to read requested files.

#### Methods

##### 1. `init_server()`

Initializes and starts the server.

```python
init_server() -> None
```

- Binds the server to the address and starts listening for connections.

##### 2. `accept_connections()`

Accepts incoming client connections.

```python
accept_connections() -> None
```

- Handles client requests in a loop until interrupted.

##### 3. `handle_client_request()`

Processes the incoming HTTP request and serves the appropriate response.

```python
handle_client_request() -> None
```

- Reads and parses the request.
- Serves files based on request paths.
- Sends appropriate error responses when necessary.

##### 4. `send_file_response()`

Sends an HTTP response with the requested file.

```python
send_file_response() -> None
```

- Constructs and sends the response with headers and body.

##### 5. `not_found_response()`

Sends a 404 Not Found response.

```python
not_found_response() -> None
```

##### 6. `illegal_method_response()`

Sends a 405 Method Not Allowed response.

```python
illegal_method_response() -> None
```

##### 7. `stop_server()`

Stops the server gracefully.

```python
stop_server() -> None
```

- Closes open sockets and terminates the server.

## Usage

1. **Run the server**

    ```bash
    python Scripts/Main.py
    ```

2. **Open a web browser and visit**:

    ```plaintext
    http://127.0.0.1:3000/
    ```

This will serve the static `index.html` file located in the `web` directory.
