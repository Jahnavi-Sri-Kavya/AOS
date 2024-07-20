import pandas as pd

def fifo_scheduling(processes):
    num_processes = len(processes)
    AT = 0
    WT = [0] * num_processes
    TAT = [0] * num_processes
    TWT = 0.0
    TTAT = 0.0
    # Calculate Waiting Time using FIFO
    for i in range(num_processes):
        WT[i] = AT
        AT += processes[i][1]
    AT = 0
    # Calculate Turn Around Time
    for i in range(num_processes):
        TAT[i] = WT[i] + processes[i][1]
    # Create DataFrame
    df = pd.DataFrame({
        'PID': [process[0] for process in processes],
        'Burst Time': [process[1] for process in processes],
        'Waiting Time': WT,
        'Turn Around Time': TAT
    })
    # Calculate Total Waiting Time
    TWT = sum(WT)
    AWT = TWT / num_processes
    # Calculate Total Turn Around Time
    TTAT = sum(TAT)
    ATAT = TTAT / num_processes
    return df, AWT, ATAT