import socket
import ssl

def start_client():
    # SSL Context setup for client-side
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations('localhost.crt')  # Use the server's certificate to verify

    # Create raw socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the client socket with SSL
    ssl_client_socket = context.wrap_socket(client_socket, server_hostname='localhost')

    try:
        # Connect to the server
        ssl_client_socket.connect(('localhost', 9999))

        # Receive the server's welcome message
        welcome_message = ssl_client_socket.recv(1024).decode()
        print(welcome_message)

        # Send 'R' for register or 'L' for login
        choice = input("Register or Login (R/L): ")
        ssl_client_socket.send(choice.encode())

        if choice.lower() == 'r':
            # Registration process
            username = input("Enter new username: ")
            ssl_client_socket.send(username.encode())

            password = input("Enter new password: ")
            ssl_client_socket.send(password.encode())

        # Login process
        username = input("Enter username: ")
        ssl_client_socket.send(username.encode())

        password = input("Enter password: ")
        ssl_client_socket.send(password.encode())

        # Receive login response
        login_response = ssl_client_socket.recv(1024).decode()
        print(login_response)

        if "Login successful" in login_response:
            while True:
                # Send messages
                message = input(f"{username}: ")
                ssl_client_socket.send(message.encode())
                
                # Receive messages
                received_message = ssl_client_socket.recv(1024).decode()
                print(received_message)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        ssl_client_socket.close()  # Ensuring the socket is always closed

if __name__ == "__main__":
    start_client()
