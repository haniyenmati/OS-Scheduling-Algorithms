import imp
from unittest import TestCase, main
from utils import input_handler
from FCFS import FCFS
from SJF import SJF
from RR import RR
from MLFQ import MLFQ

class ProjectTest(TestCase):
    def setUp(self) -> None:
        self.processes1 = input_handler('inputs/inputs.csv')

    def test_fcfs(self):
        wt_times = [3, 9, 11, 7, 20]
        tt_times = [12, 17, 23, 31, 38]
        rs_times = [0, 1, 0, 3, 7]

        fcfs = FCFS(processes=self.processes1)

        res_tt = fcfs[2]
        res_wt = fcfs[3]
        res_rs = fcfs[4]

        self.assertEqual(wt_times, res_wt)
        self.assertEqual(tt_times, res_tt)
        self.assertEqual(rs_times, res_rs)

    def test_sjf(self):
        wt_times = [3, 4, 2, 7, 20]
        tt_times = [12, 12, 14, 31, 38]
        rs_times = [0, 1, 0, 6, 11]

        fcfs = SJF(processes=self.processes1)

        res_tt = fcfs[2]
        res_wt = fcfs[3]
        res_rs = fcfs[4]

        self.assertEqual(wt_times, res_wt)
        self.assertEqual(tt_times, res_tt)
        self.assertEqual(rs_times, res_rs)

    def test_rr(self):
        wt_times = [3, 9, 11, 14, 15]
        tt_times = [12, 17, 23, 38, 33]
        rs_times = [0, 1, 0, 3, 7]

        fcfs = RR(processes=self.processes1)

        res_tt = fcfs[2]
        res_wt = fcfs[3]
        res_rs = fcfs[4]

        self.assertEqual(wt_times, res_wt)
        self.assertEqual(tt_times, res_tt)
        self.assertEqual(rs_times, res_rs)

    def test_mlfq(self):
        wt_times = [3, 9, 11, 14, 13]
        tt_times = [12, 17, 23, 38, 31]
        rs_times = [0, 1, 0, 3, 7]

        fcfs = MLFQ(processes=self.processes1)

        res_tt = fcfs[2]
        res_wt = fcfs[3]
        res_rs = fcfs[4][:5]

        self.assertEqual(wt_times, res_wt)
        self.assertEqual(tt_times, res_tt)
        self.assertEqual(rs_times, res_rs)


if __name__ == '__main__':
    main()

