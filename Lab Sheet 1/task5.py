import os, time

def cpu_task(task_id):
    """A CPU-intensive loop to simulate load."""
    s = 0
    for i in range(50_000_000):
        s += i % 3
    print(f"[Child {task_id}] PID={os.getpid()} finished work. Sum={s}")

def main():
    nice_values = [0, 5, 10]  
    children = []

    print(f"[Parent] PID={os.getpid()} creating {len(nice_values)} children...\n")

    for i, nv in enumerate(nice_values, start=1):
        pid = os.fork()
        if pid == 0:
            try:
                os.nice(nv)  
            except PermissionError:
                print(f"[Child {i}] Cannot set nice({nv}) — permission denied.")
            print(f"[Child {i}] PID={os.getpid()}, PPID={os.getppid()}, Nice={nv}")
            cpu_task(i)
            os._exit(0)
        else:
            children.append(pid)
    for pid in children:
        finished, status = os.waitpid(pid, 0)
        print(f"[Parent] Child {finished} exited with status {status}")

    print("\nAll children completed. Check execution order above.")
    print("Tip: Observe with 'top -H' or 'ps -el' while running to see priorities.")

if __name__ == "__main__":
    main()
