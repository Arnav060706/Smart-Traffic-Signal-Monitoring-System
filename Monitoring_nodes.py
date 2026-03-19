import socket
import json
import time

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open("SUMO_Simulation/Scenarios/traffic_data.json", "r") as f:
    traffic_data = json.load(f)

for record in traffic_data:

    packet = json.dumps(record)

    sock.sendto(packet.encode(), (SERVER_IP, SERVER_PORT))

    print("Sent:", record)

    time.sleep(2)  #Simulates a delay between sending data packets to the server (e.g., every 2 seconds)