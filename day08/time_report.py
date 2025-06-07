import re
from datetime import datetime
from collections import defaultdict
import os

def generate_report(log_content):
    """Generate a formatted report from log content"""
    lines = log_content.splitlines()
    
    daily_activity_list = []
    activity_time_ranges = []
    activity_total_minutes = defaultdict(int)

    for line in lines + ['']:
        match = re.match(r'(\d{2}:\d{2})\s+(.+)', line.strip())
        if match:
            time, activity_name = match.groups()
            daily_activity_list.append((time, activity_name))
        elif daily_activity_list:
            for i in range(len(daily_activity_list) - 1):
                start_time, activity_name = daily_activity_list[i]
                end_time, _ = daily_activity_list[i + 1]
                if activity_name != 'End':
                    start = datetime.strptime(start_time, '%H:%M')
                    end = datetime.strptime(end_time, '%H:%M')
                    duration = int((end - start).total_seconds() / 60)
                    activity_time_ranges.append((start_time, end_time, activity_name))
                    activity_total_minutes[activity_name] += duration
            activity_time_ranges.append(('', '', ''))  # Empty line between days
            daily_activity_list = []
    
    # Generate report
    report = []
    for start_time, end_time, activity_name in activity_time_ranges:
        if activity_name:
            report.append(f"{start_time}-{end_time} {activity_name}")
        else:
            report.append("")
    
    report.append("")  # Empty line before summary
    report.append("")  # Second empty line for spacing
    
    total_minutes = sum(activity_total_minutes.values())
    for activity_name in sorted(activity_total_minutes):
        minutes = activity_total_minutes[activity_name]
        percent = int(minutes * 100 / total_minutes)  # Using int instead of round for exact match
        report.append(f"{activity_name:<25} {minutes:>3} minutes   {percent:>2}%")
    
    return "\n".join(report)

# Example usage:
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_dir, 'examples_timelog.log')
    output_file_path = os.path.join(script_dir, 'timelog.txt')

    with open(log_file_path, 'r') as f:
        log_content = f.read()
    
    report = generate_report(log_content)
    with open(output_file_path, 'w') as f:
        f.write(report)
    
    print(f"Report saved to {output_file_path}")
