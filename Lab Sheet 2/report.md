ENCS351 - Lab 2: System Startup, Process Creation & Termination Simulation
Objective
To simulate system startup, process creation, execution, and termination using Python. This lab demonstrates how an operating system manages multiple processes and logs their lifecycle events.

Tools Used
Python 3.x
multiprocessing
logging
time
Implementation Details
Configured logging to record timestamped process activity in process_log.txt.
Defined a function system_process() to simulate a dummy task (2-second sleep).
Created two processes using multiprocessing.Process().
Used .start() to initiate and .join() to ensure graceful termination.
Verified results in log file.
Sample Output
Console:

System Starting...
System Shutdown.
process_log.txt:

2025-07-16 12:35:21,005 - Process-1 - Process-1 started
2025-07-16 12:35:21,006 - Process-2 - Process-2 started
2025-07-16 12:35:23,007 - Process-1 - Process-1 ended
2025-07-16 12:35:23,008 - Process-2 - Process-2 ended
Observations
Both processes run concurrently and finish around the same time.
The log file confirms start and end timestamps for each process.
Joining ensures all processes terminate before system shutdown.
Complexity Analysis
Time Complexity: O(n) — linear with number of processes.
Space Complexity: O(n) — due to process objects and logs.
Conclusion
This lab effectively simulates basic OS process handling. The use of multiprocessing and logging modules provides a clear, real-world demonstration of concurrent process behavior in a system startup scenario.

Author: Pravin
