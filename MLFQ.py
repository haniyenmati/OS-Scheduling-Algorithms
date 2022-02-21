from RR import fcfs_upcoming_process, rr_upcoming_process
from utils import *


def MLFQ(processes):
    arrival_time_main = [p.arrival for p in processes]
    arrival_time = arrival_time_main[::]

    cpu1_times_main = [p.cpu1 for p in processes]
    cpu1_times = cpu1_times_main[::]

    cpu2_times_main = [p.cpu2 for p in processes]
    cpu2_times = cpu2_times_main[::]

    io_time = [p.io for p in processes]

    io_finished_at = [-1 for _ in io_time]
    process_list_level_1 = [index for index in range(len(processes))]
    complete_time = [-1 for _ in io_time]
    response_time = [-1 for _ in io_time]

    process_current_status = {index: 'cpu_time' for index in range(len(processes))}

    process_list_level_2 = []
    process_list_level_3 = []

    cpu_time = 0
    counter = 0
    for i in range(len(io_time)):
        io_finished_at.append(-1)
        complete_time.append(-1)
        response_time.append(-1)
        process_list_level_1.append(i)  

    process_turn = process_list_level_1[0]

    while not process_is_complete(process_current_status):
        if len(process_list_level_1) > 0: 
            process_turn_o = fcfs_upcoming_process(arrival_time, io_finished_at)
            flag_1 = False
            if process_turn_o == process_turn:
                process_turn_o = process_list_level_1[0]
            else:
                process_turn = process_list_level_1[0]

            while process_turn_o != process_turn:
                process_list_level_1 = rr_upcoming_process(process_list_level_1)
                process_turn = process_list_level_1[-1]
                flag_1 = True

            if process_current_status[process_turn] == 'cpu_time' and arrival_time[process_turn] <= cpu_time and arrival_time[
                process_turn] != -1:
                if cpu1_times[process_turn] <= 8: 
                    temp = cpu_time - arrival_time[process_turn]
                    response_time[process_turn] = temp
                    cpu_time += cpu1_times[process_turn]
                    cpu1_times[process_turn] = 0
                    process_current_status[process_turn] = 'io_time' 
                    arrival_time[process_turn] = -1
                    io_finished_at[process_turn] = cpu_time + io_time[process_turn]
                else:  
                    temp = cpu_time - arrival_time[process_turn]
                    response_time.append(temp)
                    cpu_time += 8
                    cpu1_times[process_turn] -= 8
                    if not flag_1:
                        a = process_list_level_1.pop(0)
                    else:
                        a = process_list_level_1.pop(-1)
                    process_list_level_2.append(a)

            elif (process_current_status[process_turn] == 'io_time' or process_current_status[process_turn] == 'cpu2_time') and io_finished_at[
                process_turn] <= cpu_time and io_finished_at[
                process_turn] != -1:
                if cpu2_times[process_turn] <= 8:  
                    cpu_time += cpu2_times[process_turn]
                    cpu2_times[process_turn] = 0
                    process_current_status[process_turn] = 'complete' 
                    io_finished_at[process_turn] = -1
                    process_list_level_1.pop(-1)
                    complete_time[process_turn] = cpu_time
                else:  
                    cpu_time += 8
                    cpu2_times[process_turn] -= 8
                    process_current_status[process_turn] = 'cpu2_time'  
                    if not flag_1:
                        a = process_list_level_1.pop(0)
                    else:
                        a = process_list_level_1.pop(-1)
                    process_list_level_2.append(a)
            else:
                cpu_time += 1

        elif len(process_list_level_2) > 0:  
            flag_2 = False
            if counter == 0:
                process_turn = process_list_level_2[0]
                counter += 1
            process_turn_o = fcfs_upcoming_process(arrival_time, io_finished_at)
            if process_turn_o == process_turn:
                process_turn_o = process_list_level_2[0]
            else:
                process_turn = process_list_level_2[0]

            while process_turn_o != process_turn:  
                flag_2 = True
                process_list_level_2 = rr_upcoming_process(process_list_level_2)
                process_turn = process_list_level_2[-1]

            if process_current_status[process_turn] == 'cpu_time' and arrival_time[process_turn] <= cpu_time and arrival_time[
                process_turn] != -1:
                if cpu1_times[process_turn] <= 16:  
                    temp = cpu_time - arrival_time[process_turn]
                    response_time[process_turn] = temp
                    cpu_time += cpu1_times[process_turn]
                    cpu1_times[process_turn] = 0
                    process_current_status[process_turn] = 'io_time' 
                    arrival_time[process_turn] = -1
                    io_finished_at[process_turn] = cpu_time + io_time[process_turn]
                else:  
                    temp = cpu_time - arrival_time[process_turn]
                    response_time.append(temp)
                    cpu_time += 16
                    cpu1_times[process_turn] -= 16
                    if not flag_2:
                        a = process_list_level_2.pop(0)
                    else:
                        a = process_list_level_2.pop(-1)

                    process_list_level_3.append(a)

            elif (process_current_status[process_turn] == 'io_time' or process_current_status[process_turn] == 'cpu2_time') and io_finished_at[
                process_turn] <= cpu_time and io_finished_at[
                process_turn] != -1:
                if cpu2_times[process_turn] <= 16:  
                    cpu_time += cpu2_times[process_turn]
                    cpu2_times[process_turn] = 0
                    process_current_status[process_turn] = 'complete' 
                    io_finished_at[process_turn] = -1
                    complete_time[process_turn] = cpu_time
                    process_list_level_2.pop(-1)

                else:
                    cpu_time += 16
                    cpu2_times[process_turn] -= 16
                    process_current_status[process_turn] = 'cpu2_time'  
                    if not flag_2:
                        a = process_list_level_2.pop(0)
                    else:
                        a = process_list_level_2.pop(-1)
                    process_list_level_3.append(a)
            else:
                cpu_time += 1

        elif len(process_list_level_3) > 0:  

            process_turn = fcfs_upcoming_process(arrival_time, io_finished_at) 

            if process_current_status[process_turn] == 'cpu_time' and arrival_time[process_turn] <= cpu_time:
                temp = cpu_time - arrival_time[process_turn]
                response_time[process_turn] = temp
                cpu_time += cpu1_times[process_turn]
                process_current_status[process_turn] = 'io_time'  
                arrival_time[process_turn] = -1
                io_finished_at[process_turn] = cpu_time + io_time[process_turn]

            elif process_current_status[process_turn] == 'io_time' and io_finished_at[process_turn] <= cpu_time:
                cpu_time += cpu2_times[process_turn]
                process_current_status[process_turn] = 'complete' 
                io_finished_at[process_turn] = -1
                complete_time[process_turn] = cpu_time
                process_list_level_3.pop(-1)
            else:

                cpu_time += 1

    return arrival_time_main, complete_time, *turn_around_waiting_time(arrival_time_main, complete_time, cpu1_times_main, cpu2_times_main, io_time), response_time, cpu_time