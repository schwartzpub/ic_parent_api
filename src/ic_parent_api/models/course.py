"""Course Model Definition."""

from typing import Optional
from ic_parent_api.base import DataModel
from ic_parent_api.models.placement import Placement
from ic_parent_api.ic_api_client import CourseResponse


class Course(DataModel):
    """Course Model Definition."""

    def __init__(self, course_resp: CourseResponse):
        self._course_resp: CourseResponse = course_resp

# pylint: disable=C0103
    @property
    def id(self) -> str:
        """Property Definition."""
        return self._course_resp.id
# pylint: enable=C0103
    @property
    def roster_id(self) -> int:
        """Property Definition."""
        return self._course_resp.rosterID

    @property
    def person_id(self) -> int:
        """Property Definition."""
        return self._course_resp.personID

    @property
    def structure_id(self) -> int:
        """Property Definition."""
        return self._course_resp.structureID

    @property
    def calendar_id(self) -> int:
        """Property Definition."""
        return self._course_resp.calendarID

    @property
    def school_id(self) -> int:
        """Property Definition."""
        return self._course_resp.schoolID

    @property
    def course_name(self) -> str:
        """Property Definition."""
        return self._course_resp.courseName

    @property
    def course_number(self) -> str:
        """Property Definition."""
        return self._course_resp.courseNumber

    @property
    def is_responsive(self) -> bool:
        """Property Definition."""
        return self._course_resp.isResponsive

    @property
    def section_number(self) -> str:
        """Property Definition."""
        return self._course_resp.sectionNumber

    @property
    def end_year(self) -> str:
        """Property Definition."""
        return self._course_resp.endYear

    @property
    def school_name(self) -> str:
        """Property Definition."""
        return self._course_resp.schoolName

    @property
    def trial_id(self) -> int:
        """Property Definition."""
        return self._course_resp.trialID

    @property
    def trial_active(self) -> bool:
        """Property Definition."""
        return self._course_resp.trialActive

    @property
    def room_name(self) -> Optional[str]:
        """Property Definition."""
        return self._course_resp.roomName

    @property
    def teacher_display(self) -> Optional[str]:
        """Property Definition."""
        return self._course_resp.teacherDisplay

    @property
    def hide_standards_on_portal(self) -> bool:
        """Property Definition."""
        return self._course_resp.hideStandardsOnPortal

    @property
    def section_placements(self) -> list[Placement]:
        """Property Definition."""
        return [Placement(placement) for placement in self._course_resp.sectionPlacements]
