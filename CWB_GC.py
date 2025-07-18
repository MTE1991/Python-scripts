import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define the updated project start date
project_start_date = datetime(2025, 4, 17)

# Define updated tasks relative to new start date
tasks = [
    ("Requirement gathering & research", project_start_date, 3),
    ("UI/UX Design & Tech Stack Setup", project_start_date + timedelta(days=3), 4),
    ("Frontend Development", project_start_date + timedelta(days=7), 6),
    ("Backend Setup & Authentication", project_start_date + timedelta(days=13), 4),
    ("Crime Reporting & Map Integration", project_start_date + timedelta(days=17), 5),
    ("Analytics Dashboard & Testing", project_start_date + timedelta(days=22), 5),
    ("Bug Fixes & Optimization", project_start_date + timedelta(days=27), 3),
    ("Deployment & Documentation", project_start_date + timedelta(days=30), 3)
]

# Prepare data for plotting
start_dates = [start for _, start, _ in tasks]
durations = [duration for _, _, duration in tasks]
end_dates = [start + timedelta(days=duration) for start, duration in zip(start_dates, durations)]
task_labels = [task for task, _, _ in tasks]

# Plot the Gantt chart with start and end labels
fig, ax = plt.subplots(figsize=(10, 6))
for i, (task, start, duration) in enumerate(tasks):
    ax.barh(task_labels[i], duration, left=start, height=1, color='skyblue')
    end = start + timedelta(days=duration)
    ax.text(start - timedelta(days=0.25), i, start.strftime('%b %d'), va='center', ha='right', fontsize=10, color='black')
    ax.text(end + timedelta(days=0.25), i, end.strftime('%b %d'), va='center', ha='left', fontsize=10, color='black')

# Format chart
ax.set_xlabel("Timeline")
ax.set_title("CrimeWatch Bangladesh Project Timeline (Gantt Chart)")
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.set_xlim(project_start_date - timedelta(days=4), end_dates[-1] + timedelta(days=4))
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
