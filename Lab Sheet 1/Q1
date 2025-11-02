import os
import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 task1_fork_children.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 1:
            raise ValueError
    except ValueError:
        print("N must be a positive integer")
        sys.exit(1)

    children = []
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            mypid = os.getpid()
            ppid = os.getppid()
            print(f"[Child {i+1}] PID: {mypid}, PPID: {ppid} -> Hello from child #{i+1}")
            time.sleep(0.1)
            os._exit(0)
        else:
            children.append(pid)
            
    print(f"[Parent] spawned {len(children)} children, waiting for them to finish...")
    while True:
        try:
            pid, status = os.wait()
            print(f"[Parent] child {pid} exited with status {status}")
        except ChildProcessError:
            break

    print("[Parent] all children have finished. Exiting.")

if __name__ == "__main__":
    main()
