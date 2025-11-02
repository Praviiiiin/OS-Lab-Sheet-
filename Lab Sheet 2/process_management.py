Sub-Task 1: Initialize the logging configuration
Objective: Set up the logging system to log messages with timestamps and process names.
import logging
# Setup logger
logging.basicConfig(
    filename='process_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

  
  Sub-Task 2: Define a function that simulates a process task
Objective: Write a function that mimics the work of a system process.
import time
# Dummy function to simulate a task
def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate task delay
    logging.info(f"{task_name} ended")
  

Sub-Task 3: Create at least two processes and start them concurrently
Objective: Use the multiprocessing module to initiate parallel tasks.
import multiprocessing
if __name__ == '__main__':
    print("System Starting...")
    # Create processes
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))
    # Start processes
    p1.start()
    p2.start()


Sub-Task 4: Ensure proper termination and verify logs
Objective: Wait for processes to complete and confirm the shutdown.
    # Wait for processes to complete
    p1.join()
    p2.join()
    print("System Shutdown.")
