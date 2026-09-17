from datetime import datetime

def find_peak_usage(logs):
    hourly_counts = [0] * 24

    for log in logs:
        time = datetime.fromisoformat(log)
        hour = time.hour
        hourly_counts[hour] += 1

    peak_hour = 0

    for hour in range(1, 24):
        if hourly_counts[hour] > hourly_counts[peak_hour]:
            peak_hour = hour

    return peak_hour


logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T13:45:10",
    "2026-08-04T09:15:30",
    "2026-08-04T13:50:25",
    "2026-08-04T09:30:12",
    "2026-08-04T18:10:45"
]

result = find_peak_usage(logs)
print("Peak usage hour:", result)
