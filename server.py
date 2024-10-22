import socket
import ssl
import threading

clients = {}
user_credentials = {}

def handle_client(client_socket, client_address, ssl_client_socket):
    try:
        client_socket.send("Welcome! Register or Login (R/L): ".encode())
        choice = ssl_client_socket.recv(1024).decode()

        if choice.lower() == 'r':
            ssl_client_socket.send("Enter new username: ".encode())
            username = ssl_client_socket.recv(1024).decode()

            ssl_client_socket.send("Enter new password: ".encode())
            password = ssl_client_socket.recv(1024).decode()

            user_credentials[username] = password
            ssl_client_socket.send("Registration successful. Please login.".encode())

        ssl_client_socket.send("Enter username: ".encode())
        username = ssl_client_socket.recv(1024).decode()

        ssl_client_socket.send("Enter password: ".encode())
        password = ssl_client_socket.recv(1024).decode()

        if username in user_credentials and user_credentials[username] == password:
            ssl_client_socket.send("Login successful! You can now send messages.".encode())
            clients[username] = ssl_client_socket
            while True:
                message = ssl_client_socket.recv(1024).decode()
                print(f"Message from {username}: {message}")

                # Echo the message back to all clients
                for client_user, client_conn in clients.items():
                    if client_user != username:
                        client_conn.send(f"{username}: {message}".encode())
        else:
            ssl_client_socket.send("Invalid login.".encode())
            ssl_client_socket.close()

    except Exception as e:
        print(f"Error with client {client_address}: {e}")
        ssl_client_socket.close()

def start_server():
    # Set up SSL context for server
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="localhost.crt", keyfile="localhost.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)

    print("[*] Server listening on port 9999")

    while True:
        client_socket, addr = server_socket.accept()
        ssl_client_socket = context.wrap_socket(client_socket, server_side=True)
        print(f"[*] Accepted connection from {addr}")

        client_handler = threading.Thread(
            target=handle_client, args=(client_socket, addr, ssl_client_socket)
        )
        client_handler.start()

if __name__ == "__main__":
    start_server()
