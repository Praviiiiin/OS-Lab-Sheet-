
import os
import sys

def read_status(pid):
    path = f"/proc/{pid}/status"
    info = {}
    try:
        with open(path, 'r') as f:
            for line in f:
                if line.startswith("Name:"):
                    info['Name'] = line.split()[1]
                elif line.startswith("State:"):
                    info['State'] = " ".join(line.split()[1:])
                elif line.startswith("VmSize:"):
                    info['VmSize'] = " ".join(line.split()[1:])
                elif line.startswith("VmRSS:"):
                    info['VmRSS'] = " ".join(line.split()[1:])
    except FileNotFoundError:
        raise FileNotFoundError(f"/proc/{pid} does not exist or access denied")
    return info

def read_exe(pid):
    try:
        exe_path = os.readlink(f"/proc/{pid}/exe")
        return exe_path
    except FileNotFoundError:
        raise FileNotFoundError(f"/proc/{pid}/exe not found")
    except PermissionError:
        return "<permission denied>"

def read_fds(pid):
    fd_dir = f"/proc/{pid}/fd"
    fds = {}
    try:
        for fdname in os.listdir(fd_dir):
            full = os.path.join(fd_dir, fdname)
            try:
                target = os.readlink(full)
            except OSError:
                target = "<cannot readlink>"
            fds[fdname] = target
    except FileNotFoundError:
        raise FileNotFoundError(f"/proc/{pid}/fd not found or access denied")
    except PermissionError:
        return {"error": "<permission denied>"}
    return fds

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 task4_proc_inspect.py PID")
        sys.exit(1)
    pid = sys.argv[1]
    if not pid.isdigit():
        print("PID must be numeric")
        sys.exit(1)

    try:
        status = read_status(pid)
        exe = read_exe(pid)
        fds = read_fds(pid)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    print(f"Process /proc/{pid} info:")
    print("-" * 40)
    print(f"Name:  {status.get('Name', 'N/A')}")
    print(f"State: {status.get('State', 'N/A')}")
    print(f"VmSize: {status.get('VmSize', 'N/A')}")
    print(f"VmRSS: {status.get('VmRSS', 'N/A')}")
    print(f"Executable: {exe}")
    print("-" * 40)
    print("Open file descriptors:")
    if isinstance(fds, dict) and fds:
        for fd, target in sorted(fds.items(), key=lambda t: int(t[0]) if t[0].isdigit() else t[0]):
            print(f"  fd {fd}: {target}")
    else:
        print("  <no fds or cannot access>")

if __name__ == "__main__":
    main()
