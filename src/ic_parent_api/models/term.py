"""Term Model Definition."""

from datetime import date
from ic_parent_api.base import DataModel
from ic_parent_api.ic_api_client import TermResponse


class Term(DataModel):
    """Term Model Definition."""

    def __init__(self, term_resp: TermResponse):
        self._id = term_resp.id
        self._term_id = term_resp.termID
        self._term_schedule_id = term_resp.termScheduleID
        self._seq = term_resp.seq
        self._start_date = term_resp.startDate
        self._end_date = term_resp.endDate
        self._term_name = term_resp.termName
        self._structure_id = term_resp.structureID
        self._is_primary = term_resp.isPrimary
        self._term_schedule_name = term_resp.termScheduleName
        self._calendar_id = term_resp.calendarID
        self._schedule_structure_name = term_resp.scheduleStructureName

    @property
    def id(self) -> str:
        """Property Definition."""
        return self._id

    @property
    def term_id(self) -> int:
        """Property Definition."""
        return self._term_id

    @property
    def term_schedule_id(self) -> int:
        """Property Definition."""
        return self._term_schedule_id

    @property
    def seq(self) -> int:
        """Property Definition."""
        return self._seq

    @property
    def start_date(self) -> date:
        """Property Definition."""
        return self._start_date

    @property
    def end_date(self) -> date:
        """Property Definition."""
        return self._end_date

    @property
    def term_name(self) -> str:
        """Property Definition."""
        return self._term_name

    @property
    def structure_id(self) -> int:
        """Property Definition."""
        return self._structure_id

    @property
    def is_primary(self) -> bool:
        """Property Definition."""
        return self._is_primary

    @property
    def term_schedule_name(self) -> str:
        """Property Definition."""
        return self._term_schedule_name

    @property
    def calendar_id(self) -> int:
        """Property Definition."""
        return self._calendar_id

    @property
    def schedule_structure_name(self) -> str:
        """Property Definition."""
        return self._schedule_structure_name
