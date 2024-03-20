class Process:
    process_id = 0
    arrival_time = 0
    cpu_burst_time1 = 0
    cpu_burst_time2 = 0
    io_time = 0
    title = "Placeholder"

    def __init__(self, process_id, arrival_time, cpu_time1, io_time, cpu_time2, title):
        self.arrival_time = arrival_time
        self.cpu_burst_time1 = cpu_time1
        self.cpu_burst_time2 = cpu_time2
        self.io_time = io_time
        self.process_id = process_id
        self.title = str(title)

    def __repr__(self):
        return ("Arrival time: " + str(self.arrival_time) +
               "\nCPU Burst time 1: " + str(self.cpu_burst_time1) +
               "\nCPU Burst time 2: " + str(self.cpu_burst_time2) +
               "\nIO Time: " + str(self.io_time) +
               "\nProcess ID: " + str(self.process_id) +
               "\nTitle: " + str(self.title)) + "\n"
