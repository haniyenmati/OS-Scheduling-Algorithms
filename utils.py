import csv
from Process import Process


def process_is_complete(process_turn_state: dict):
    return all([state=='complete' for state in process_turn_state.values()])

def turn_around_waiting_time(arrival: list, complete_time: list, cpu1: list, cpu2: list, io: list):
    turn_around, waiting = [], []

    for i in range(len(arrival)):
        temp = complete_time[i] - arrival[i]
        turn_around.append(temp)
        burst_total = cpu1[i] + cpu2[i]
        temp = turn_around[i] - burst_total - io[i]
        waiting.append(temp)

    return turn_around, waiting


def process_output_template(arrival_time, complete_time, turn_around_time, waiting_time, response_time, total_time, burst_time_1, burst_time_2):
    total_response = 0
    total_turnaround = 0
    total_waiting = 0
    total_burst_time = 0
    count_processes = len(arrival_time)

    
    print("\tResponseTime\t\tTurnAroundTime\t\tWaitingTime\t\tArrivalTime\t\tCompleteTime")
    for i in range(count_processes):
        print(
            f"P{i+1}\t\t{response_time[i]}\t\t\t{turn_around_time[i]}\t\t\t{waiting_time[i]}\t\t\t{arrival_time[i]}\t\t\t{complete_time[i]}")
        total_response += response_time[i]
        total_turnaround += turn_around_time[i]
        total_waiting += waiting_time[i]
        total_burst_time += burst_time_1[i] + burst_time_2[i]

    print("~~~~~~~~~~~~~~-----------~~~~~~~~~~~~~------------~~~~~~~~~~~~~----------~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print(f"Average\t\t{total_response / count_processes}\t\t\t{total_turnaround / count_processes}\t\t\t{total_waiting / count_processes}")
    print(f"\ntotal time => {total_time}")

    print(f"total burst time => {total_burst_time}")
    print(f"idle => {total_time - total_burst_time}")
    
    print(f"cpu utilization => {round((total_burst_time / total_time), 3) * 100} %")
    print(f"troughput = {round(((count_processes * 1000) / total_time), 3)}")


def input_handler(input_path):
    file = open(input_path)
    processes_data = csv.reader(file)

    # after getting rows names, theres only data remaining
    processes_data.__next__()
    processes = [ Process(int(row[1]), int(row[2]), int(row[3]), int(row[4])) for row in processes_data]
    return processes


if __name__ == '__main__':
    print(input_handler('Data/inputs.csv'))