import socket
import threading


# Function to handle client connections
def handle_client(client_socket, client_address):
    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print("Client {}: {}".format(client_address, message))

        # Send message to client
        reply = input("You: ")
        client_socket.send(reply.encode())


# Set up server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "127.0.0.11"
server_port = 1023
server_socket.bind((server_host, server_port))
server_socket.listen(5)

print("Server listening on {}:{}".format(server_host, server_port))

# Accept incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    print("Connected to client:", client_address)

    # Create a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
