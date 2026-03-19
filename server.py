import socket
import json

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("Traffic Monitoring Server Running...")

intersection_status = {}

def analyze_congestion(queue_length, waiting_time):

    if queue_length < 5:
        return "NORMAL"

    elif queue_length < 15:
        return "MODERATE CONGESTION"

    else:
        return "SEVERE CONGESTION"


while True:

    data, addr = sock.recvfrom(65535)

    packet = json.loads(data.decode())
    print(packet)
    intersection_id = "SILK BOARD"  # Placeholder for intersection ID, can be extracted from packet if available
    queue_length = (
    packet["north_queue"] +
    packet["south_queue"] +
    packet["east_queue"] +
    packet["west_queue"])
    waiting_time = packet["waiting_time"]

    status = analyze_congestion(queue_length, waiting_time)

    intersection_status[intersection_id] = packet

    print("Received data from:", intersection_id)
    print("Queue length:", queue_length)
    print("Waiting time:", waiting_time)
    print("Traffic Status:", status)

    if status == "SEVERE CONGESTION":
        print("🚨 ALERT: Severe congestion detected!")