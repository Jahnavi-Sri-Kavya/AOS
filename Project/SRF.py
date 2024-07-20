import pandas as pd

def srf_scheduling(processes):
    num_processes = len(processes)
    remaining_time = [proc[1] for proc in processes]  # Burst times
    arrival_time = [proc[2] for proc in processes]
    completion_time = [0] * num_processes
    waiting_time = [0] * num_processes
    turnaround_time = [0] * num_processes
    time = 0
    completed = 0
    # List to keep track of whether a process has been executed
    is_completed = [False] * num_processes
    while completed < num_processes:
        # Find the process with the smallest remaining time
        min_time = float('inf')
        min_index = -1
        for i in range(num_processes):
            if arrival_time[i] <= time and not is_completed[i] and remaining_time[i] < min_time:
                min_time = remaining_time[i]
                min_index = i
        if min_index != -1:
            # Execute the process with the smallest remaining time
            remaining_time[min_index] -= 1
            time += 1
            # If the process is completed
            if remaining_time[min_index] == 0:
                completion_time[min_index] = time
                is_completed[min_index] = True
                completed += 1
        else:
            # If no process is ready to execute, move forward in time
            time += 1
    # Calculate Waiting Time and Turnaround Time
    for i in range(num_processes):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
    # Create DataFrame
    df = pd.DataFrame({
        'PID': [proc[0] for proc in processes],
        'Arrival Time': arrival_time,
        'Burst Time': [proc[1] for proc in processes],
        'Completion Time': completion_time,
        'Waiting Time': waiting_time,
        'Turnaround Time': turnaround_time
    })
    # Calculate Average Waiting Time and Turnaround Time
    AWT = sum(waiting_time) / num_processes
    ATAT = sum(turnaround_time) / num_processes
    return df, AWT, ATAT

