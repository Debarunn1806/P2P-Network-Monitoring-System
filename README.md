# Peer-to-Peer Network Monitoring System

A Python-based peer-to-peer (P2P) network monitoring system that facilitates connection monitoring, message exchange, and round-trip time (RTT) calculation between two peers. The project demonstrates a basic peer-to-peer communication model with robust error handling for a seamless user experience.

## Features
- Establishes a peer-to-peer connection between two clients.
- Allows users to send messages with timestamps.
- Calculates and displays Round Trip Time (RTT) for each message exchange.
- Provides online/offline status for the peer connection.
- Includes error handling for connection issues, message sending failures, and unexpected socket closures.

## How It Works

- **Listener**: One thread listens for incoming connections and handles received messages, calculates RTT when a message is received, and displays the result.
- **Sender**: Another thread allows the user to send messages and calculates the RTT for each message exchange.
- **Error Handling**: The system incorporates error handling to manage issues like offline peers, connection errors, and socket-related errors.

## Error Handling

The code includes comprehensive error handling to ensure stable operation and smooth user experience:

1. **Peer Offline**: If the sender attempts to connect and finds the peer offline, the program will display a message: `"Status: Your peer is OFFline"`, allowing the sender to retry or quit gracefully.

2. **Connection Errors**: When a connection attempt fails due to network issues or incorrect details, the program catches the error, logs it, and notifies the user without crashing.

3. **Socket Closure**: Ensures that sockets are properly closed after each message exchange to avoid resource leaks. The code safely handles socket shutdown and closure with `try-except-finally` blocks to ensure all resources are released even if errors occur.

## Usage

1. Start the program in two terminals and input the following details:
   - **Your Name**: Identifier for each peer.
   - **Your Port**: The port number unique to each instance.
   - **Peer's IP and Port**: Use `localhost` or `127.0.0.1` for IP and a different port number for the peer.

2. After setup, choose to either:
   - **Send a message**: Enter `Y` or `y` to send a message and calculate RTT.
   - **Quit**: Enter `N` or `n` to terminate the connection.

Upon sending a message, the program calculates the RTT once the peer responds.

### Example Interaction

Example interaction in each terminal instance:

```plaintext
Y or y to send message, N or n to quit: y
Status: Your peer is ONLINE.
Waiting for the response to finish...

Received message from Peer1
Total Round Trip Time (RTT): X.XXXX seconds
