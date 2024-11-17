---
icon: fontawesome/solid/bug
hide:
  - toc
---

# Debugging

___

To enable debugging and view more detailed logs, simply set the `log_level` to `DEBUG`.

```python
from reminder import Reminder, Schedule
from datetime import timedelta
from logging import DEBUG

# Initialize the reminder system
reminder = Reminder()

# Add a schedule with a 1-minute timer
reminder.add_schedule('Task 1: Timer for 1 minute', timedelta(minutes=1))

# Event handler for when the system is initialized
@reminder.event
async def on_initiate():
    print(f"Reminder system has been successfully initialized!")

# Event handler for when a schedule is triggered
@reminder.event
async def on_schedule(schedule: Schedule):
    print(f"Triggered schedule: {schedule.title}")

# Run the reminder system with debug logging enabled
reminder.run(log_level=DEBUG)
