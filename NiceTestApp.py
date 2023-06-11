import platform
import psutil
import argparse
import os
import subprocess

def fetch_computer_name():
    return platform.node()

def fetch_total_physical_memory():
    mem = psutil.virtual_memory()
    return f"{mem.total // (1024 ** 3)} Gb"

def fetch_total_physical_processors():
    return psutil.cpu_count(logical=False)

def fetch_total_cores():
    return psutil.cpu_count(logical=True)

def fetch_total_hard_disks():
    return len(psutil.disk_partitions(all=False))

def fetch_top_cpu_processes(num_processes=5):
    ps_command = "ps -eo pid,%cpu,comm --sort=-%cpu | head -n {}".format(num_processes + 1)
    result = subprocess.check_output(ps_command, shell=True, universal_newlines=True)
    lines = result.strip().split("\n")[1:]  # Skip the header line
    processes = []
    for line in lines:
        pid, cpu_percent, name = line.strip().split(None, 2)
        processes.append((name, float(cpu_percent)))
    return processes

def print_on_screen():
    computer_name = fetch_computer_name()
    total_memory = fetch_total_physical_memory()
    total_processors = fetch_total_physical_processors()
    total_cores = fetch_total_cores()
    total_disks = fetch_total_hard_disks()
    top_processes = fetch_top_cpu_processes()

    print(f"Computer Name: {computer_name}")
    print(f"Total Physical Memory: {total_memory}")
    print(f"Total Number of Physical Processors: {total_processors}")
    print(f"Total Number of Cores: {total_cores}")
    print(f"Total Number of Hard Disks: {total_disks}")
    print("Top 5 processes in terms of CPU:")
    for process, cpu_percent in top_processes:
        print(f"\t{process}: {cpu_percent}%")

def log_to_file():
    computer_name = fetch_computer_name()
    total_memory = fetch_total_physical_memory()
    total_processors = fetch_total_physical_processors()
    total_cores = fetch_total_cores()
    total_disks = fetch_total_hard_disks()
    top_processes = fetch_top_cpu_processes()

    log_file = os.path.splitext(os.path.basename(__file__))[0] + ".log"
    with open(log_file, 'w') as f:
        f.write(f"Computer Name: {computer_name}\n")
        f.write(f"Total Physical Memory: {total_memory}\n")
        f.write(f"Total Number of Physical Processors: {total_processors}\n")
        f.write(f"Total Number of Cores: {total_cores}\n")
        f.write(f"Total Number of Hard Disks: {total_disks}\n")
        f.write("Top 5 processes in terms of CPU:\n")
        for process, cpu_percent in top_processes:
            f.write(f"\t{process}: {cpu_percent}%\n")

def print_help():
    print("NiceTestApp.py")
    print("This application provides information about the computer.")
    print("Arguments:")
    print("-logInfo\tOutputs information to a log file")
    print("-help\t\tDisplays this help message")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-logInfo", action="store_true", help="Outputs information to a log file")
    parser.add_argument("-help", action="store_true", help="Displays help message")
    args = parser.parse_args()

    if args.help:
        print_help()
    elif args.logInfo:
        print_on_screen()
        log_to_file()
    else:
        print_on_screen()

if __name__ == "__main__":
    main()
