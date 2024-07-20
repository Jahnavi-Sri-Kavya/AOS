import streamlit as st
import matplotlib.pyplot as plt
import random
import RR as r
import SJF as sjf
import SRF as srf
import FIFO as fifo
import priority as p


print(" ")
print("My student id: 16325267. Last 2 digits are 6 and 7. So, ")
# Generate 67 processes with random burst times between 1 and 10
print(" ")
processes = [[i + 1, random.randint(1, 10)] for i in range(67)]
print("Number of processes = ", len(processes))
print(" ")
print("----------First Come First Serve--------------")
df1, AWT1, ATAT1 = fifo.fifo_scheduling(processes)
excel_file = 'fcfs_scheduling.xlsx'
df1.to_excel(excel_file, index=False)
print(", ".join(f"p{pid}" for pid in df1['PID']))
print(f"Average Waiting Time: {AWT1:.2f}")
print(f"Average Turn Around Time: {ATAT1:.2f}")
print(" ")
print("------------Shortest Job First---------")
df2, AWT2, ATAT2 = sjf.sjf_scheduling(processes)
excel_file = 'sjf_scheduling.xlsx'
df2.to_excel(excel_file, index=False)
print(", ".join(f"p{pid}" for pid in df2['PID']))
print(f"Average Waiting Time: {AWT2:.2f}")
print(f"Average Turn Around Time: {ATAT2:.2f}")
print(" ")
print("------------Round Robin with Quantum 6ms---------")
df5, AWT5, ATAT5 = r.RR_scheduling(processes,6)
excel_file = 'rr_scheduling.xlsx'
df5.to_excel(excel_file, index=False)
print(", ".join(f"p{pid}" for pid in df5['PID']))
print(f"Average Waiting Time: {AWT5:.2f}")
print(f"Average Turn Around Time: {ATAT5:.2f}")
print(" ")
arrival_times = [random.randint(1, 10) for _ in range(67)]
for i in range(len(processes)):
    processes[i].append(arrival_times[i])
sorted_processes = sorted(processes, key=lambda x: x[0])
print("------------Shortest Remaining Time First---------")
df3, AWT3, ATAT3 = srf.srf_scheduling(sorted_processes)
excel_file = 'srf_scheduling.xlsx'
df3.to_excel(excel_file, index=False)
print(", ".join(f"p{pid}" for pid in df3['PID']))
print(f"Average Waiting Time: {AWT3:.2f}")
print(f"Average Turn Around Time: {ATAT3:.2f}")
print(" ")
print("-----------Priority Scheduling----------")
df4, AWT4, ATAT4 = p.priority_scheduling(sorted_processes)
excel_file = 'priority_scheduling.xlsx'
df4.to_excel(excel_file, index=False)
print(", ".join(f"p{pid}" for pid in df4['PID']))
print(f"Average Waiting Time: {AWT4:.2f}")
print(f"Average Turn Around Time: {ATAT4:.2f}")
print(" ")