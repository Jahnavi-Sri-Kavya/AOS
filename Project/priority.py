import pandas as pd

def priority_scheduling(processes):
    num_processes = len(processes)
    AT = 0
    WT = [0] * num_processes
    TAT = [0] * num_processes
    TWT = 0.0
    TTAT = 0.0
    # Sort processes based on Priority (smallest value has highest priority)
    processes.sort(key=lambda x: x[2]) 
    # Calculate Waiting Time
    for i in range(num_processes):
        WT[i] = AT
        AT += processes[i][1]
    # Calculate Turn Around Time
    for i in range(num_processes):
        TAT[i] = WT[i] + processes[i][1]
    # Create DataFrame
    df = pd.DataFrame({
        'PID': [proc[0] for proc in processes],
        'Burst Time': [proc[1] for proc in processes],
        'Priority': [proc[2] for proc in processes],
        'Waiting Time': WT,
        'Turn Around Time': TAT
    })
    # Calculate Average Waiting Time and Turnaround Time
    TWT = sum(WT)
    AWT = TWT / num_processes
    TTAT = sum(TAT)
    ATAT = TTAT / num_processes
    return df, AWT, ATAT