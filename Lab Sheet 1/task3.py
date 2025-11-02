import os
import time
import sys

def main():
    pid = os.fork()
    if pid == 0:
        print(f"[Child] PID {os.getpid()} exiting immediately (becomes zombie until parent collects).")
        os._exit(0)
    else:
        print(f"[Parent] PID {os.getpid()} created child {pid}. Parent will sleep for 20s (not calling wait()).")
        print("Run in another terminal: ps -el | grep defunct  (or: ps aux | grep Z)")
        try:
            time.sleep(20)
        except KeyboardInterrupt:
            pass
        try:
            wpid, status = os.wait()
            print(f"[Parent] waited and collected child {wpid} with status {status}")
        except ChildProcessError:
            print("[Parent] no child to wait for")
        print("[Parent] exiting.")

if __name__ == "__main__":
    main()
