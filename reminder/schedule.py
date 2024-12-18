"""
The MIT License (MIT)

Copyright (c) 2024-present Snifo

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime
    from datetime import timedelta
    from typing import Optional

__all__ = ('Schedule',)


class Schedule:
    """
    Represents a schedule.

    Parameters
    ----------
    _id: str
        A unique identifier for the schedule.
    title: str
        The title of the schedule.
    duration: timedelta
        The duration of the schedule.
    created_at: datetime
        The datetime when the schedule was created.
    description: Optional[str]
        A description of the schedule.
    callback: Optional[str]
        A callback event name to be executed when the schedule ends.
    """

    __slots__ = ('id', 'title', 'description', 'created_at', 'ends_at', 'callback')

    def __init__(self,
                 _id: str,
                 /,
                 title: str,
                 duration: timedelta,
                 created_at: datetime,
                 description: Optional[str] = None,
                 callback: Optional[str] = None,
                 )-> None:
        self.id: str = _id
        self.title: str = title
        self.description: Optional[str] = description
        self.created_at: datetime = created_at
        self.ends_at: datetime = self.created_at + duration
        self.callback: Optional[str] = callback

    def is_active(self, current_time: datetime) -> bool:
        """
        Check if the schedule is active.

        Parameters
        ----------
        current_time: datetime
            The current time to compare with `ends_at`.

        Returns
        -------
        bool
            True if the schedule is active, otherwise False.
        """
        return self.created_at <= current_time < self.ends_at


    def __repr__(self) -> str:
        """
        Returns a string representation of the schedule.

        Returns
        -------
        str
            A string representation of the schedule.
        """
        return (f"<Schedule(title={self.id!r}, title={self.title!r}, description={self.description!r}, "
                f"created_at={self.created_at}, ends_at={self.ends_at}, "
                f"callback={self.callback})>")