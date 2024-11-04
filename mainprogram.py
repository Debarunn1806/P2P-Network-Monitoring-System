# Importing required libraries
import socket
import threading
import time

# Initializing required global variables
ENCODING = 'utf-8'
flag = True
globalCurrentTime = None
globalReceivedTime = None
turnBoolean = True

# Inputs required
print("-----------------------------------")
myName = input("My Name: ")
myIP = "localhost"
myPort = int(input("My Port: "))


def main():
    """Main function to make threads and call sender and receiver thread."""
    # Peer information inputs
    print("-----------------------------------")
    peerName = input("Enter Peer's Name: ")
    peerIP = input("Peer's IP: ")
    peerPort = int(input("Peer's Port: "))
    print("-----------------------------------")
    print()

    # Initializing threads
    if flag:
        receiverThread = threading.Thread(target=listen, args=(myIP, myPort))
    senderThread = threading.Thread(target=send, args=(peerIP, peerPort))

    # Starting threads
    if flag:
        receiverThread.start()
    senderThread.start()

    # Joining threads
    if flag:
        receiverThread.join()
    senderThread.join()


def listen(myIP, myPort):
    """Function for Listener."""
    global globalCurrentTime, globalReceivedTime, turnBoolean

    # Establishing connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((myIP, myPort))
        sock.listen(10)
        print(f"Listening on {myIP}:{myPort}...")
    except Exception as e:
        print(f"Error setting up listener on {myIP}:{myPort} - {e}")
        return

    # Always trying to connect
    while True:
        try:
            connection, client_address = sock.accept()
            print(f"Connected by {client_address}")

            receivedMessage = ""

            # Always listening once established
            while True:
                receivedTime = time.time()
                globalReceivedTime = receivedTime
                data = connection.recv(16)

                if data:
                    receivedMessage += data.decode(ENCODING)
                else:
                    if globalCurrentTime is not None and globalReceivedTime is not None:
                        print(receivedMessage.strip())
                        print("Total Round Trip Time (RTT): " + 
                              str(globalReceivedTime - globalCurrentTime) + " seconds")
                        globalCurrentTime = None
                        globalReceivedTime = None
                        turnBoolean = True
                        print("\n")
                    break

        except Exception as e:
            print(f"Error during receiving: {e}")
        finally:
            connection.close()


def send(peerIP, peerPort):
    """Function for Sender."""
    global globalCurrentTime, globalReceivedTime, turnBoolean

    while True:
        breakOuter = False
        while turnBoolean:
            option = input("Y or y to send message, N or n to quit: ")

            if option.lower() == "n":
                global flag
                flag = False
                breakOuter = True
                break

            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((peerIP, peerPort))

                if result == 0:
                    print("Status: Your peer is ONLINE.")
                    currentTime = time.time()
                    messageWithTimeStamp = "Time Stamp: " + myName + " : " + str(currentTime)
                    globalCurrentTime = currentTime

                    try:
                        s.sendall(messageWithTimeStamp.encode(ENCODING))
                    except Exception as e:
                        print(f"Error sending message: {e}")
                        turnBoolean = True
                        continue

                    turnBoolean = False
                    print("Message sent. Waiting for response...")
                else:
                    print("Status: Your peer is OFFLINE.")
                
            except socket.error as e:
                print(f"Socket error: {e}")
            finally:
                s.close()

        if breakOuter:
            break

    # Attempt to connect to another peer after quitting
    main()

# Calling main function
if __name__ == "__main__":
    main()
