
import psutil


# Function to save process information into a log file
def save_log(message):
    with open("logs/process_monitor.log", "a") as log_file:
        log_file.write(message + "\n")


# Function to monitor running processes
def monitor_processes():

    print("=" * 60)
    print("          TOP 5 PROCESSES BY CPU USAGE")
    print("=" * 60)

    processes = []

    # Collect information about running processes
    for process in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_percent']
    ):
        try:
            processes.append(process.info)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort processes by CPU usage
    processes.sort(
        key=lambda process: process['cpu_percent'] or 0,
        reverse=True
    )

    # Display top 5 processes and save to log
    for process in processes[:5]:

        message = (
            f"PID: {process['pid']} | "
            f"Name: {process['name']} | "
            f"CPU: {process['cpu_percent']}% | "
            f"Memory: {process['memory_percent']:.2f}%"
        )

        print(message)
        save_log(message)

    print("=" * 60)


# Main program execution
if __name__ == "__main__":
    monitor_processes()

