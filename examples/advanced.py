from reminder import Reminder, Schedule
from datetime import timedelta
import asyncio

class Remind(Reminder):
    def __init__(self):
        super().__init__(cycle=350)

    def do_stuff(self):
        """Some Stuff"""
        self.add_schedule('Task 1: Timer for 1 minute', timedelta(minutes=1))
        self.add_schedule('Task 2: Reminder in 5 seconds', timedelta(seconds=5), description='Juice up.')
        self.add_schedule('Task 3: Another reminder in 30 seconds', timedelta(seconds=30))
        self.add_schedule('Task 4: Another reminder in 8 seconds', timedelta(seconds=8), callback='xyz')

    async def start(self):
        """Initialize event loop and start the reminder controller"""
        self.initiate_event_loop()
        task = self.loop.create_task(self.controller.initiate())

        # Some stuff.
        self.do_stuff()

        # Run the task asynchronously and allow other operations to continue
        await asyncio.gather(task)

    async def on_error(self, event_name: str, error: Exception, /, *args, **kwargs) -> None:
        """Handle errors during event execution."""
        print(f"An error occurred in event '{event_name}': {error}")

    async def on_initiate(self):
        print(f"Reminder has been initiated")

    async def on_schedule(self, schedule: Schedule):
        print(f"Triggered schedule: {schedule}")

    async def on_xyz(self, schedule: Schedule):
        print(f"Triggered schedule on xyz: {schedule}")
        self.remove_schedule_by_title('Task 1: Timer for 1 minute')
        print(f"Left schedules: {self.get_schedules()}")

# Initialize and run the Remind system
reminder_system = Remind()
reminder_system.run()
