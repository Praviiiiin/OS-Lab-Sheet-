import time
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)
def system_process(task_name):
    """Simulates a small system process task."""
    logging.info(f"{task_name} started")
    time.sleep(2)  
    logging.info(f"{task_name} ended")
system_process("Process-1")
