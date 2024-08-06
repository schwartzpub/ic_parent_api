"""Placement Model Definition."""

from typing import Optional

from ic_parent_api.base import DataModel
from ic_parent_api.models.base import PlacementResponse
from ic_parent_api.models.term import Term


class Placement(DataModel):
    """Placement Model Definition."""

    def __init__(self, placement_resp: PlacementResponse):
        self._placement_resp: PlacementResponse = placement_resp

    @property
    def placement_id(self) -> str:
        """Property Definition."""
        return self._placement_resp.id

    @property
    def section_id(self) -> int:
        """Property Definition."""
        return self._placement_resp.sectionID

    @property
    def term_id(self) -> int:
        """Property Definition."""
        return self._placement_resp.termID

    @property
    def term_name(self) -> str:
        """Property Definition."""
        return self._placement_resp.termName

    @property
    def term_seq(self) -> int:
        """Property Definition."""
        return self._placement_resp.termSeq

    @property
    def period_id(self) -> int:
        """Property Definition."""
        return self._placement_resp.periodID

    @property
    def trial_id(self) -> int:
        """Property Definition."""
        return self._placement_resp.trialID

    @property
    def period_sequence(self) -> int:
        """Property Definition."""
        return self._placement_resp.periodSequence

    @property
    def term(self) -> Term:
        """Property Definition."""
        return Term(self._placement_resp.term)

    @property
    def period_schedule_id(self) -> int:
        """Property Definition."""
        return self._placement_resp.periodScheduleID

    @property
    def start_time(self) -> Optional[str]:
        """Property Definition."""
        return self._placement_resp.startTime

    @property
    def end_time(self) -> Optional[str]:
        """Property Definition."""
        return self._placement_resp.endTime

    @property
    def period_name(self) -> str:
        """Property Definition."""
        return self._placement_resp.periodName

    @property
    def period_schedule_name(self) -> str:
        """Property Definition."""
        return self._placement_resp.periodScheduleName

    @property
    def teacher_display(self) -> Optional[str]:
        """Property Definition."""
        return self._placement_resp.teacherDisplay

    @property
    def period_schedule_sequence(self) -> int:
        """Property Definition."""
        return self._placement_resp.periodScheduleSequence

    @property
    def structure_id(self) -> int:
        """Property Definition."""
        return self._placement_resp.structureID

    @property
    def course_id(self) -> int:
        """Property Definition."""
        return self._placement_resp.courseID

    @property
    def course_number(self) -> str:
        """Property Definition."""
        return self._placement_resp.courseNumber

    @property
    def section_number(self) -> int:
        """Property Definition."""
        return self._placement_resp.sectionNumber

    @property
    def course_name(self) -> str:
        """Property Definition."""
        return self._placement_resp.courseName

    @property
    def term_schedule_id(self) -> int:
        """Property Definition."""
        return self._placement_resp.termScheduleID

    @property
    def start_date(self) -> str:
        """Property Definition."""
        return self._placement_resp.startDate

    @property
    def end_date(self) -> str:
        """Property Definition."""
        return self._placement_resp.endDate

    @property
    def room_id(self) -> Optional[int]:
        """Property Definition."""
        return self._placement_resp.roomID

    @property
    def room_name(self) -> Optional[str]:
        """Property Definition."""
        return self._placement_resp.roomName

    @property
    def unit_attendance(self) -> Optional[bool]:
        """Property Definition."""
        return self._placement_resp.unitAttendance

    @property
    def attendance(self) -> bool:
        """Property Definition."""
        return self._placement_resp.attendance

    @property
    def is_responsive(self) -> bool:
        """Property Definition."""
        return self._placement_resp.isResponsive
