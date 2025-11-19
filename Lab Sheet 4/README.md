🖥️ Operating System Lab – Advanced Simulation (Batch Processing, System Calls, VM Check, Scheduling)

This repository contains Python and Shell scripts that simulate various advanced Operating System concepts.
Each task demonstrates how OS handles batch processing, system startup, system calls, inter-process communication, virtualization checks, and CPU scheduling algorithms.

📌 Task 1 – Batch Processing Simulation (Python)

Simulates batch processing systems where multiple scripts are executed sequentially.

⭐ Features

Executes multiple .py programs one after another

Uses subprocess module to mimic real batch execution

Displays script execution order

Code Highlights

List of script names stored in an array

Iterative execution using subprocess.call()

📌 Task 2 – System Startup and Logging

Simulates a system boot process using multiprocessing and logs events into a file.

⭐ Features

Creates multiple Python processes (like OS services)

Logs:

Process Start

Process End

Stores logs inside system_log.txt

Uses multiprocessing and logging

Real-World Analogy

Acts like Linux services starting during boot and writing entries in /var/log/syslog.

📌 Task 3 – System Calls & IPC (fork, exec, wait, pipe)

Implements low-level system calls using Python's os module, similar to C programs.

⭐ Features

Uses:

fork() → Creates child process

exec() → Executes a new program (if added)

wait() → Parent waits for child

pipe() → Communication channel

⭐ IPC Demonstration

Parent sends a message through a pipe

Child receives and prints it

Real-World Use

This demonstrates how Linux processes communicate (e.g., shell pipelines).

📌 Task 4 – VM Detection & Shell Interaction
Part A – Shell Script

Displays system information such as:

✔ Kernel Version
✔ Username
✔ Virtualization Support (lscpu output)

Part B – Python VM Detection

Python script checks if the system is running inside a virtual machine using hardware flags.

⭐ Features

Reads CPU virtualization features

Helps identify if the OS runs under VirtualBox/VMware/KVM

📌 Task 5 – CPU Scheduling Algorithms (Python)

Implements major scheduling algorithms to calculate:

Waiting Time (WT)

Turnaround Time (TAT)

Gantt Order

Algorithms Included

✔ FCFS – First Come First Serve
✔ SJF – Shortest Job First
✔ Round Robin
✔ Priority Scheduling

⭐ Features

Accepts burst time, priority, and time quantum

Calculates WT & TAT for each process

Prints averages
