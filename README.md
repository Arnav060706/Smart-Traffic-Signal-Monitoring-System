# Smart-Traffic-Signal-Monitoring-System

Traffic Signal Monitoring system to identify the varying congestion rates during numerous traffic simulations likening to real-life

Project Overview:<br>
The Smart Traffic Monitoring System is a network-based traffic monitoring application that simulates road traffic conditions and transmits real-time traffic data to a central monitoring server. The system uses traffic simulation, network communication, and data analysis to detect congestion and display the traffic conditions.

The traffic environment is simulated using SUMO (Simulation of Urban Mobility). Traffic data is extracted from the simulation using TraCI (Traffic Control Interface), processed using Python, and then transmitted to a central monitoring server using UDP socket communication to ensure fast and low latency communication.

The central server analyzes the received traffic data and determines congestion levels based on parameters such as queue length and vehicle waiting time. The system then displays the traffic status on a simple monitoring dashboard made using Tkinter

Objectives:<br>
1) Simulate realistic traffic conditions at an intersection. <br>
2) Extract traffic information from the simulation environment.<br>
3) Transmit traffic updates over a network using UDP.<br>
4) Implement a central monitoring server that analyzes traffic conditions.<br>
5) Detect and display congestion alerts in real time.<br>
