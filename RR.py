from utils import *
from FCFS import fcfs_upcoming_process

def rr_upcoming_process(processes):
    return processes[1:] + processes[0:1]

def RR(processes):
    QUANTUM = 5

    arrival_time_main = [p.arrival for p in processes]
    arrival_time = arrival_time_main[::]

    cpu1_times_main = [p.cpu1 for p in processes]
    cpu1_times = cpu1_times_main[::]

    cpu2_times_main = [p.cpu2 for p in processes]
    cpu2_times = cpu2_times_main[::]

    io_time = [p.io for p in processes]

    process_end_time = [-1 for _ in io_time]
    process_list = [index for index in range(len(processes))]
    complete_time = [-1 for _ in io_time]
    response_time = [-1 for _ in io_time]

    process_current_status = {index: 'cpu_time' for index in range(len(processes))}

    cpu_time = 0
    process_turn = 0
    process_turn = process_list[0]

    
    while not process_is_complete(process_current_status):
        process_turn_o = fcfs_upcoming_process(arrival_time, process_end_time)
        if process_turn_o == process_turn:
            process_turn_o = process_list[0]
            
        else:
            process_turn = process_list[0]

        while process_turn_o != process_turn:
            process_list = rr_upcoming_process(process_list)
            process_turn = process_list[-1]

        if process_current_status[process_turn] == 'cpu_time' and arrival_time[process_turn] <= cpu_time and arrival_time[process_turn] != -1:
            
            if cpu1_times[process_turn] <= QUANTUM:
                temp = cpu_time - arrival_time[process_turn]
                response_time[process_turn] = temp
                cpu_time += cpu1_times[process_turn]
                cpu1_times[process_turn] = 0

                process_current_status[process_turn] = 'io_time'
                arrival_time[process_turn] = -1
                process_end_time[process_turn] = cpu_time + io_time[process_turn]

            else:
                temp = cpu_time - arrival_time[process_turn]
                response_time.append(temp)
                cpu_time += QUANTUM
                cpu1_times[process_turn] -= QUANTUM

        elif (process_current_status[process_turn] == 'io_time' or process_current_status[process_turn] == 'cpu2_time')\
        and process_end_time[process_turn] <= cpu_time and process_end_time[process_turn] != -1:
        
            if cpu2_times[process_turn] <= QUANTUM:
                cpu_time += cpu2_times[process_turn]
                cpu2_times[process_turn] = 0
                process_current_status[process_turn] = 'complete'
                process_end_time[process_turn] = -1
                complete_time[process_turn] = cpu_time

            else:
                cpu_time += QUANTUM
                cpu2_times[process_turn] -= QUANTUM
                process_current_status[process_turn] = 'cpu2_time'
        else:
            cpu_time += 1

    return arrival_time_main, complete_time, *turn_around_waiting_time(arrival_time_main, complete_time, cpu1_times_main, cpu2_times_main, io_time), response_time, cpu_time