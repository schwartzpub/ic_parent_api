"""Term Model Definition."""
from ic_parent_api.base import DataModel
from ic_parent_api.ic_api_client import TermResponse


class Term(DataModel):
    """Term Model Definition."""
    def __init__(self, term_resp: TermResponse):
        self._id = term_resp.id
        self._termid = term_resp.termID
        self._termscheduleid = term_resp.termScheduleID
        self._seq = term_resp.seq
        self._startdate = term_resp.startDate
        self._enddate = term_resp.endDate
        self._termname = term_resp.termName
        self._structureid = term_resp.structureID
        self._isprimary = term_resp.isPrimary
        self._termschedulename = term_resp.termScheduleName
        self._calendarid = term_resp.calendarID
        self._schedulestructurename = term_resp.scheduleStructureName

    @property
    def id(self) -> str:
        """Property Definition."""
        return self._id

    @property
    def termid(self) -> int:
        """Property Definition."""
        return self._termid

    @property
    def termscheduleid(self) -> int:
        """Property Definition."""
        return self._termscheduleid

    @property
    def seq(self) -> int:
        """Property Definition."""
        return self._seq

    @property
    def startdate(self) -> str:
        """Property Definition."""
        return self._startdate

    @property
    def enddate(self) -> str:
        """Property Definition."""
        return self._enddate

    @property
    def termname(self) -> str:
        """Property Definition."""
        return self._termname

    @property
    def structureid(self) -> int:
        """Property Definition."""
        return self._structureid

    @property
    def isprimary(self) -> bool:
        """Property Definition."""
        return self._isprimary

    @property
    def termschedulename(self) -> str:
        """Property Definition."""
        return self._termschedulename

    @property
    def calendarid(self) -> int:
        """Property Definition."""
        return self._calendarid

    @property
    def schedulestructurename(self) -> str:
        """Property Definition."""
        return self._schedulestructurename
