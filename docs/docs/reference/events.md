---
icon: material/clock-time-eleven-outline
---

# Event Handlers

___

- `on_initiate`
    - **Description**: Triggered when the event system is initialized.
    - **Usage**:
    ```python
    @client.event
    async def on_initiate() -> None:
        # Add your code here to handle the event when initialization completes
        ...
    ```

---

- `on_schedule`
    - **Description**: Triggered when a scheduled time is reached.
    - **Data Type**: [`Schedule`][reminder.schedule.Schedule]
    - **Usage**:
    ```python
    @client.event
    async def on_schedule(schedule: Schedule) -> None:
        # Handle actions when a schedule is triggered
        ...
    ```
