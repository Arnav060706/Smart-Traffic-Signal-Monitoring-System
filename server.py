import socket
import json
import os

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("🚦 Smart Traffic Monitoring Server Started...\n")

def analyze_congestion(queue, wait):

    if queue < 5 and wait < 10:
        return "NORMAL"

    elif queue < 15:
        return "MODERATE CONGESTION"

    else:
        return "SEVERE CONGESTION"


while True:

    data, addr = sock.recvfrom(65535)
    packet = json.loads(data.decode())

    north = packet["north_queue"]
    south = packet["south_queue"]
    east = packet["east_queue"]
    west = packet["west_queue"]

    total_queue = north + south + east + west
    waiting_time = packet["waiting_time"]

    status = analyze_congestion(total_queue, waiting_time)

    os.system("cls" if os.name == "nt" else "clear")

    print("🚦 TRAFFIC MONITORING DASHBOARD")
    print("---------------------------------\n")

    print("Intersection : SILK BOARD CROSS")
    print("Time         :", packet["timestamp"])
    print("Vehicles     :", packet["vehicle_count"])
    print()

    print("Queue Lengths")
    print("North :", north)
    print("South :", south)
    print("East  :", east)
    print("West  :", west)
    print()

    print("Total Queue  :", total_queue)
    print("Waiting Time :", waiting_time)
    print("Signal State :", packet["signal_state"])
    print()

    print("🚦 Traffic Status :", status)

    if status == "SEVERE CONGESTION":
        print("\n🚨 ALERT: Severe congestion detected!")