from utils import *


def fcfs_upcoming_process(arrive, complete):
    arrival_min, arrival_index = least_arrival_time(arrive)
    io_min, io_index = least_arrival_time(complete)
    
    if arrival_min > io_min:
        return io_index
    return arrival_index


def least_arrival_time(arrival):
    """
        we are implementing Fist-Come-First-Serve!
        So, we need to order processes by their arival time, first.
    """
    minimum_index, minimum_val = 0, 10000000000 # maximum amount so it will change each time
    
    for i in range(len(arrival)):
        if (arrival[i] < minimum_val) and (arrival[i] != -1):
            minimum_val = arrival[i]
            minimum_index = i

    return minimum_val, minimum_index


def FCFS(processes):
    arrival_time_main = [p.arrival for p in processes]
    cpu1_times = [p.cpu1 for p in processes]
    cpu2_times = [p.cpu2 for p in processes]
    io_time = [p.io for p in processes]

    arrival_time = arrival_time_main[::]
    process_end_time = [-1 for _ in io_time]
    complete_time = [-1 for _ in io_time]
    response_time = [-1 for _ in io_time]

    process_current_status = {index: 'cpu_time' for index in range(len(processes))}
    cpu_time = 0

    while not process_is_complete(process_current_status):
        process_turn = fcfs_upcoming_process(arrival_time, process_end_time)

        if process_current_status[process_turn] == 'cpu_time' and arrival_time[process_turn] <= cpu_time:
            temp = cpu_time - arrival_time[process_turn]
            response_time[process_turn] = temp
            cpu_time += cpu1_times[process_turn]
            process_current_status[process_turn] = 'io_time' 
            arrival_time[process_turn] = -1
            process_end_time[process_turn] = cpu_time + io_time[process_turn]

        elif process_current_status[process_turn] == 'io_time' and process_end_time[process_turn] <= cpu_time:
            cpu_time += cpu2_times[process_turn]
            process_current_status[process_turn] = 'complete'
            process_end_time[process_turn] = -1
            complete_time[process_turn] = cpu_time
            
        else:
            cpu_time += 1    

    return arrival_time_main, complete_time, *turn_around_waiting_time(arrival_time_main, complete_time, cpu1_times, cpu2_times, io_time), response_time, cpu_time