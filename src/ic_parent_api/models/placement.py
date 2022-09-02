"""Placement Model Definition."""
from ic_parent_api.base import DataModel
from ic_parent_api.ic_api_client import PlacementResponse
from ic_parent_api.models.term import Term


class Placement(DataModel):
    """Placement Model Definition."""
    def __init__(self, placement_resp: PlacementResponse):
        self._id = placement_resp.id
        self._sectionid = placement_resp.sectionID
        self._termid = placement_resp.termID
        self._termname = placement_resp.termName
        self._termseq = placement_resp.termSeq
        self._periodid = placement_resp.periodID
        self._trialid = placement_resp.trialID
        self._periodsequence = placement_resp.periodSequence
        self._term = placement_resp.term
        self._periodscheduleid = placement_resp.periodScheduleID
        self._starttime = placement_resp.startTime
        self._endtime = placement_resp.endTime
        self._periodname = placement_resp.periodName
        self._periodschedulename = placement_resp.periodScheduleName
        self._teacherdisplay = placement_resp.teacherDisplay
        self._periodschedulesequence = placement_resp.periodScheduleSequence
        self._structureid = placement_resp.structureID
        self._courseid = placement_resp.courseID
        self._coursenumber = placement_resp.courseNumber
        self._sectionnumber = placement_resp.sectionNumber
        self._coursename = placement_resp.courseName
        self._termscheduleid = placement_resp.termScheduleID
        self._startdate = placement_resp.startDate
        self._enddate = placement_resp.endDate
        self._roomid = placement_resp.roomID
        self._roomname = placement_resp.roomName
        self._unitattendance = placement_resp.unitAttendance
        self._attendance = placement_resp.attendance
        self._isresponsive = placement_resp.isResponsive

    @property
    def id(self) -> str:
        """Property Definition."""
        return self._id

    @property
    def sectionid(self) -> int:
        """Property Definition."""
        return self._sectionid

    @property
    def termid(self) -> int:
        """Property Definition."""
        return self._termid

    @property
    def termname(self) -> str:
        """Property Definition."""
        return self._termname

    @property
    def termseq(self) -> int:
        """Property Definition."""
        return self._termseq

    @property
    def periodid(self) -> int:
        """Property Definition."""
        return self._periodid

    @property
    def trialid(self) -> int:
        """Property Definition."""
        return self._trialid

    @property
    def periodsequence(self) -> int:
        """Property Definition."""
        return self._periodsequence

    @property
    def term(self) -> Term:
        """Property Definition."""
        return Term(self._term)

    @property
    def periodscheduleid(self) -> int:
        """Property Definition."""
        return self._periodscheduleid

    @property
    def starttime(self) -> str:
        """Property Definition."""
        return self._starttime

    @property
    def endtime(self) -> str:
        """Property Definition."""
        return self._endtime

    @property
    def periodname(self) -> str:
        """Property Definition."""
        return self._periodname

    @property
    def periodschedulename(self) -> str:
        """Property Definition."""
        return self._periodschedulename

    @property
    def teacherdisplay(self) -> str:
        """Property Definition."""
        return self._teacherdisplay

    @property
    def periodschedulesequence(self) -> int:
        """Property Definition."""
        return self._periodschedulesequence

    @property
    def structureid(self) -> int:
        """Property Definition."""
        return self._structureid

    @property
    def courseid(self) -> int:
        """Property Definition."""
        return self._courseid

    @property
    def coursenumber(self) -> str:
        """Property Definition."""
        return self._coursenumber

    @property
    def sectionnumber(self) -> int:
        """Property Definition."""
        return self._sectionnumber

    @property
    def coursename(self) -> str:
        """Property Definition."""
        return self._coursename

    @property
    def termscheduleid(self) -> int:
        """Property Definition."""
        return self._termscheduleid

    @property
    def startdate(self) -> str:
        """Property Definition."""
        return self._startdate

    @property
    def enddate(self) -> str:
        """Property Definition."""
        return self._enddate

    @property
    def roomid(self) -> int:
        """Property Definition."""
        return self._roomid

    @property
    def roomname(self) -> str:
        """Property Definition."""
        return self._roomname

    @property
    def unitattendance(self) -> bool:
        """Property Definition."""
        return self._unitattendance

    @property
    def attendance(self) -> bool:
        """Property Definition."""
        return self._attendance

    @property
    def isresponsive(self) -> bool:
        """Property Definition."""
        return self._isresponsive
