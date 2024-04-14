import socket
import threading

# Function to receive messages from the server
def receive_messages():
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print("Server:", message)

# Set up client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "127.0.0.11"
server_port = 1023
client_socket.connect((server_host, server_port))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Send messages to server
while True:
    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break

# Close client socket
client_socket.close()
