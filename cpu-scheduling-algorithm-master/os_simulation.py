import sys

sys.path.append(".")
from Data_Collector import DataCollector
from FCFS_algo import FCFS
from Grantt_Analysis import GranttAnalysis
from SJF_algo import SJF
from MLFQ_algo import MLFQ
from Process import Process
from RR_algo import RoundRobin
from GPT4_algo import GPT4S
from Gemini_algo import GeminiS

csv_input_path = 'test/Set0_CPU_Time1ver2.csv'

while True:
    print('\033[94m' + '------------------------------------------------------------')
    print('FCFS = 1 | SJF = 2 | RR = 3 | MLFQ = 4 | CGPTS = 5 | GS = 6')
    print('------------------------------------------------------------' + '\033[0m')
    data_collector = []
    try:
        mode = int(input('Enter: '))
    except Exception as error:
        print('\033[93m' + 'Error: Wrong Input!')
        exit(-1)
    data_collector = DataCollector(csv_path=csv_input_path)
    # ------- get a deep copy of processes -------
    processes_copy = []
    result = None
    print("File being executed: " + csv_input_path + "\n")
    for process in data_collector.getProcesses().copy():
        processes_copy.append(Process(process.process_id,
                                      process.arrival_time,
                                      process.cpu_burst_time1,
                                      process.io_time,
                                      process.cpu_burst_time2,
                                      process.title))
    if mode == 1:
        # ------------------- FCFS -------------------
        result = FCFS(processes=data_collector.getProcesses())
        grantt_chart = result.cpu_process()
    elif mode == 2:
        # ------------------- SJF --------------------
        result = SJF(processes=data_collector.getProcesses())
        grantt_chart = result.cpu_process()
    elif mode == 3:
        # ------------------- RR ---------------------
        result = RoundRobin(processes=data_collector.getProcesses().copy())
        grantt_chart = result.cpu_process(time_quantum=1)
    elif mode == 4:
        # ------------------ MLFQ --------------------
        result = MLFQ(processes=data_collector.getProcesses().copy())
        grantt_chart = result.cpu_process()
    elif mode == 5:
        print("ChatGPT Scheduler not yet implemented")
        result = GPT4S(processes=data_collector.getProcesses().copy())
        grantt_chart = result.cpu_process(time_quantum=1)
    elif mode == 6:
        print("Gemini Scheduler not yet implemented")
        result = GeminiS(processes=data_collector.getProcesses().copy())
        grantt_chart = result.cpu_process(time_quantum=1)
    else:
        exit(0)
    if result is not None:
        analysis = GranttAnalysis(grantt_chart=result.grantt_chart, processes=processes_copy)
        analysis.pretty_print(result.ClassName)
