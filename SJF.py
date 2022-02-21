from utils import *

def sort_sjf_by_arrival_time(arrive, burst):
    return [i for i in range(len(arrive)) if arrive[i] <= burst and arrive[i] != -1]

def sjf_upcoming_process(arrive, complete, burst1, burst2, cpu_tot):
    arrive_list = sort_sjf_by_arrival_time(arrive, cpu_tot)
    complete_io_list = sort_sjf_by_arrival_time(complete, cpu_tot)

    is_arrived = False
    arrive_index, minimum_val = 0, 10000000

    if len(arrive_list) > 1:
        for i in arrive_list:
            if burst1[i] < minimum_val:
                minimum_val = burst1[i]
                arrive_index = i
                is_arrived = True

    elif len(arrive_list) == 1:
        arrive_index = arrive_list[0]
        is_arrived = True

    io_completed = False
    minimum_val, min_index_io_finished = 10000000000, 0

    if len(complete_io_list) > 1:
        for i in range(len(complete_io_list)):
            if burst2[i] < minimum_val:
                minimum_val = burst2[i]
                min_index_io_finished = i
                io_completed = True

    elif len(complete_io_list) == 1:
        min_index_io_finished = complete_io_list[0]
        io_completed = True

    if is_arrived and io_completed:
        if burst1[arrive_index] <= burst2[min_index_io_finished]:
            return arrive_index

        else:
            return min_index_io_finished

    elif not is_arrived and io_completed:
        return min_index_io_finished

    elif is_arrived and not io_completed:
        return arrive_index
        
    return 0


def SJF(processes):
    arrival_time_main = [p.arrival for p in processes]
    arrival_time = arrival_time_main[::]

    cpu1_times_main = [p.cpu1 for p in processes]
    cpu2_times_main = [p.cpu2 for p in processes]
    io_time = [p.io for p in processes]

    process_io_time = [-1 for _ in io_time]
    complete_time = [-1 for _ in io_time]
    response_time = [-1 for _ in io_time]

    process_current_status = {index: 'cpu_time' for index in range(len(processes))}

    cpu_time = 0
    while not process_is_complete(process_current_status):
        process_turn = sjf_upcoming_process(arrival_time, process_io_time, cpu1_times_main, cpu2_times_main, cpu_time)

        if process_current_status[process_turn] == 'cpu_time' and arrival_time[process_turn] <= cpu_time:
            temp = cpu_time - arrival_time[process_turn]
            response_time[process_turn] = temp
            cpu_time += cpu1_times_main[process_turn]
            process_current_status[process_turn] = 'io_time'
            arrival_time[process_turn] = -1
            process_io_time[process_turn] = cpu_time + io_time[process_turn]

        elif process_current_status[process_turn] == 'io_time' and process_io_time[process_turn] <= cpu_time:
            cpu_time += cpu2_times_main[process_turn]
            process_current_status[process_turn] = 'complete'
            process_io_time[process_turn] = -1
            complete_time[process_turn] = cpu_time

        else:
            cpu_time += 1    

    return arrival_time_main, complete_time, *turn_around_waiting_time(arrival_time_main, complete_time, cpu1_times_main, cpu2_times_main, io_time), response_time, cpu_time