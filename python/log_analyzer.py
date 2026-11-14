
import os
from datetime import datetime

LOG_FILE = "/var/log/syslog"
REPORT_FILE = "reports/log_analysis_report.txt"


def analyze_logs():

    print("=" * 60)
    print("             LINUX LOG ANALYZER")
    print("=" * 60)

    if not os.path.exists(LOG_FILE):
        print("ERROR: Log file not found!")
        return

    total_lines = 0
    error_count = 0
    warning_count = 0
    info_count = 0

    with open(LOG_FILE, "r", errors="replace") as log_file:

        for line in log_file:

            total_lines += 1

            if "error" in line.lower():
                error_count += 1

            elif "warning" in line.lower():
                warning_count += 1

            elif "info" in line.lower():
                info_count += 1

    analysis_time = datetime.now()

    # Prepare report content
    report = (
        "LINUX LOG ANALYSIS REPORT\n"
        "=" * 50 + "\n"
        f"Analysis Time: {analysis_time}\n"
        f"Log File: {LOG_FILE}\n\n"
        "--- LOG SUMMARY ---\n"
        f"Total Log Entries: {total_lines}\n"
        f"Errors: {error_count}\n"
        f"Warnings: {warning_count}\n"
        f"Info Messages: {info_count}\n\n"
        "--- LOG HEALTH ---\n"
        + (
            "WARNING: Errors detected in system logs!\n"
            if error_count > 0
            else "System logs look healthy.\n"
        )
    )

    # Display report in terminal
    print(report)

    # Save report to file
    with open(REPORT_FILE, "w") as report_file:
        report_file.write(report)

    print(f"Report saved successfully: {REPORT_FILE}")


if __name__ == "__main__":
    analyze_logs()
