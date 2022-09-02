"""ScheduleDay Model Definition."""
from ic_parent_api.base import DataModel
from ic_parent_api.ic_api_client import ScheduleDayResponse


class ScheduleDay(DataModel):
    """ScheduleDay Model Definition."""
    def __init__(self, scheduleday_resp: ScheduleDayResponse):
        self._id = scheduleday_resp.id
        self._dayid = scheduleday_resp.dayID
        self._calendarid = scheduleday_resp.calendarID
        self._structureid = scheduleday_resp.structureID
        self._periodscheduleid = scheduleday_resp.periodScheduleID
        self._date = scheduleday_resp.date
        self._requiresattendance = scheduleday_resp.requiresAttendance
        self._isschoolday = scheduleday_resp.isSchoolDay
        self._duration = scheduleday_resp.duration
        self._trialid = scheduleday_resp.trialID

    @property
    def id(self) -> str:
        """Property Definition."""
        return self._id

    @property
    def dayid(self) -> int:
        """Property Definition."""
        return self._dayid

    @property
    def calendarid(self) -> int:
        """Property Definition."""
        return self._calendarid

    @property
    def structureid(self) -> int:
        """Property Definition."""
        return self._structureid

    @property
    def periodscheduleid(self) -> int:
        """Property Definition."""
        return self._periodscheduleid

    @property
    def date(self) -> str:
        """Property Definition."""
        return self._date

    @property
    def requiresattendance(self) -> bool:
        """Property Definition."""
        return self._requiresattendance

    @property
    def isschoolday(self) -> bool:
        """Property Definition."""
        return self._isschoolday

    @property
    def duration(self) -> int:
        """Property Definition."""
        return self._duration

    @property
    def trialid(self) -> int:
        """Property Definition."""
        return self._trialid
