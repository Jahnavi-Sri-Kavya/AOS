import pandas as pd

def RR_scheduling(processes, quantum):
    num_processes = len(processes)
    AT = 0
    WT = [0] * num_processes
    TAT = [0] * num_processes
    RBT = [0] * num_processes
    CT = [0] * num_processes
    s = [0] * num_processes
    TWT = 0.0
    TTAT = 0.0
    # Initialize Remaining Burst Time
    for i in range(num_processes):
        RBT[i] = processes[i][1]
    time = 0
    pi = 0
    while True:
        if s[pi] == 0:
            if RBT[pi] > quantum:
                RBT[pi] -= quantum
                time += quantum
            else:
                time += RBT[pi]
                RBT[pi] = 0
                s[pi] = 1
                CT[pi] = time
        else:
            if pi + 1 < num_processes:
                pi += 1
            else:
                pi = 0
            continue
        if pi + 1 < num_processes:
            pi += 1
        else:
            pi = 0
        if all(status == 1 for status in s):
            break
    # Calculate Waiting Time and Turn Around Time
    for i in range(num_processes):
        WT[i] = CT[i] - processes[i][1]
        TAT[i] = processes[i][1] + WT[i]
    # Create DataFrame
    df = pd.DataFrame({
        'PID': [proc[0] for proc in processes],
        'Burst Time': [proc[1] for proc in processes],
        'Remaining Burst Time': RBT,
        'Completion Time': CT,
        'Status': s,
        'Waiting Time': WT,
        'Turn Around Time': TAT
    })
    # Calculate Average Waiting Time and Turnaround Time
    TWT = sum(WT)
    AWT = TWT / num_processes
    TTAT = sum(TAT)
    ATAT = TTAT / num_processes
    return df, AWT, ATAT

