from reminder import Reminder, Schedule
from datetime import timedelta

reminder = Reminder()

reminder.add_schedule('Task 1: Timer for 1 minute', timedelta(minutes=1))
reminder.add_schedule('Task 2: Reminder in 30 seconds', timedelta(seconds=30), callback='task_reminder')
reminder.add_schedule('Task 3: Another reminder in 30 seconds', timedelta(seconds=30), callback='task_reminder')

@reminder.event
async def on_initiate():
    print(f"Reminder has been initiated")

@reminder.event
async def on_schedule(schedule: Schedule):
    print(f"Triggered schedule: {schedule.title}")

@reminder.event
async def on_task_reminder(schedule: Schedule):
    print(f"Custom reminder callback triggered for schedule: {schedule.title}")

reminder.run()
