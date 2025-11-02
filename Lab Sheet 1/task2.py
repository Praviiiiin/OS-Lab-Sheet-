import os
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 task2_execvp_children.py N command [args...]")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be integer")
        sys.exit(1)

    cmd = sys.argv[2]
    args = sys.argv[2:]  

    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print(f"[Child {i+1}] PID {os.getpid()} executing: {' '.join(args)}")
            try:
                os.execvp(cmd, args)
            except FileNotFoundError:
                print(f"Command not found: {cmd}")
                os._exit(127)
        else:
            pass
    while True:
        try:
            pid, status = os.wait()
            print(f"[Parent] child {pid} exited with status {status}")
        except ChildProcessError:
            break

if __name__ == "__main__":
    main()
