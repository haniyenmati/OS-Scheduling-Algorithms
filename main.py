from FCFS import FCFS
from MLFQ import MLFQ
from RR import RR
from SJF import SJF
from utils import *


def main():
    END_FLAG = True

    while(END_FLAG):

        path = input('enter the csv file path as input: ')
        process_input = input_handler(path)

        # cpu times seperated
        cpu1_times = [process.cpu1 for process in process_input]
        cpu2_times = [process.cpu2 for process in process_input]

        alg = input('FCFS?: (y/n)')

        if alg=='y':
            fcfs = FCFS(processes=process_input)
            print("\n\n=============----------------===============-------------====================-----------==============")
            print("\t\t\t\t\tscheduling algorithm : FCFS")
            print("=============----------------===============-------------====================-----------==============")
            process_output_template(*fcfs, cpu1_times, cpu2_times)

        alg = input('RR?: (y/n)')
        if alg=='y':
            rr = RR(processes=process_input)
            print("\n\n=============----------------===============-------------====================-----------==============")
            print("\t\t\t\t\tscheduling algorithm : RoundRobin, q=5ms")
            print("=============----------------===============-------------====================-----------==============")
            process_output_template(*rr, cpu1_times, cpu2_times)

        alg = input('SJF?: (y/n)')
        if alg=='y':
            sjf = SJF(processes=process_input)
            print("\n\n=============----------------===============-------------====================-----------==============")
            print("\t\t\t\t\tscheduling algorithm : SJF")
            print("=============----------------===============-------------====================-----------==============")
            process_output_template(*sjf, cpu1_times, cpu2_times )


        alg = input('MLFQ?: (y/n)')
        if alg=='y':
            mlfq = MLFQ(processes=process_input)
            print("\n\n=============----------------===============-------------====================-----------==============")
            print("\t\t\t\t\tscheduling algorithm : MLFQ (FCFS, RR)")
            print("=============----------------===============-------------====================-----------==============")
            process_output_template(*mlfq, cpu1_times, cpu2_times)

        do = input('do you want ot try another process?: (y/n)')
        if do=='n':
            break


if __name__ == '__main__':
    main()