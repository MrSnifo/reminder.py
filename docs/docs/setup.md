---
icon: fontawesome/solid/turn-up
hide:
  - toc
---

## Setting Up reminder.py

To get started with `reminder.py`, follow these steps to install and create reminders.

### Install reminder.py

Ensure you have `pip` installed, then run the following command in your terminal or command prompt:

#### On Windows

```bash
py -3 -m pip install -U reminder.py
```

#### On Linux/macOS

```bash
python3 -m pip install -U reminder.py
```

### Clone (Optional)

!!! Info
    Cloning the repository is for accessing beta releases.

```shell
git clone https://github.com/MrSnifo/reminder.py.git
```

### Create a Reminder System

Once installed, you can create a reminder system as shown in the example below:

```python
from reminder import Reminder, Schedule
from datetime import timedelta

reminder = Reminder()
reminder.add_schedule('Task 1: 1-minute timer', timedelta(minutes=1))

@reminder.event
async def on_initiate():
    print("Reminder initiated")

@reminder.event
async def on_schedule(schedule: Schedule):
    print(f"Triggered: {schedule.title}")

reminder.run()
```

For more details and examples, visit the [examples repository](https://github.com/MrSniFo/reminder.py/tree/main/examples).