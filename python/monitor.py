
import psutil
import platform
from datetime import datetime

def get_system_metrics():
    print("=" * 50)
    print("       LINUX SERVER MONITORING SYSTEM")
    print("=" * 50)

    print(f"Timestamp: {datetime.now()}")
    print(f"Hostname: {platform.node()}")
    print(f"Operating System: {platform.system()}")

    # CPU Monitoring
    cpu_usage = psutil.cpu_percent(interval=1)

    # Memory Monitoring
    memory = psutil.virtual_memory()

    # Disk Monitoring
    disk = psutil.disk_usage("/")

     # Prepare monitoring data
    timestamp = datetime.now()

    log_message = (
        f"{timestamp} | "
        f"CPU: {cpu_usage}% | "
        f"Memory: {memory.percent}% | "
        f"Disk: {disk.percent}%"
    )

    # Save monitoring data
    save_to_log(log_message)

    print("\n--- SYSTEM HEALTH ---")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Memory Available: {memory.available / (1024**3):.2f} GB")
    print(f"Disk Usage: {disk.percent}%")
    print(f"Disk Free: {disk.free / (1024**3):.2f} GB")

  

    print("\n--- HEALTH STATUS ---")

    if cpu_usage > 80:
        print("WARNING: High CPU Usage")
    else:
        print("CPU Status: NORMAL")

    if memory.percent > 80:
        print("WARNING: High Memory Usage")
    else:
        print("Memory Status: NORMAL")

    if disk.percent > 80:
        print("WARNING: High Disk Usage")
    else:
        print("Disk Status: NORMAL")

    print("=" * 50)

def save_to_log(message):
    with open("logs/system_monitor.log", "a") as log_file:
        log_file.write(message + "\n")

if __name__ == "__main__":
    get_system_metrics()

