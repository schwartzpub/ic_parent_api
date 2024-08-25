"""Enrollment Model Definition."""

from typing import Optional
from ic_parent_api.base import DataModel
from ic_parent_api.models.base import EnrollmentResponse


class Enrollment(DataModel):
    """Enrollment Model Definition."""

    def __init__(self, enrollment_resp: EnrollmentResponse):
        self._enrollment_resp: EnrollmentResponse = enrollment_resp

    @property
    def enrollment_id(self) -> int:
        """Property Definition."""
        return self._enrollment_resp.enrollmentID

    @property
    def person_id(self) -> int:
        """Property Definition."""
        return self._enrollment_resp.personID

    @property
    def structure_id(self) -> int:
        """Property Definition."""
        return self._enrollment_resp.structureID

    @property
    def structure_name(self) -> str:
        """Property Definition."""
        return self._enrollment_resp.structureName

    @property
    def district_id(self) -> int:
        """Property Definition."""
        return self._enrollment_resp.districtID

    @property
    def end_year(self) -> int:
        """Property Definition."""
        return self._enrollment_resp.endYear

    @property
    def service_type(self) -> str:
        """Property Definition."""
        return self._enrollment_resp.serviceType

    @property
    def start_date(self) -> str:
        """Property Definition."""
        return self._enrollment_resp.startDate

    @property
    def end_date(self) -> Optional[str]:
        """Property Definition."""
        return self._enrollment_resp.endDate

    @property
    def grade(self) -> str:
        """Property Definition."""
        return self._enrollment_resp.grade

    @property
    def school_id(self) -> int:
        """Property Definition."""
        return self._enrollment_resp.schoolID

    @property
    def school_name(self) -> str:
        """Property Definition."""
        return self._enrollment_resp.schoolName

    @property
    def show_on_portal(self) -> bool:
        """Property Definition."""
        return self._enrollment_resp.showOnPortal

    @property
    def future_show_on_portal(self) -> bool:
        """Property Definition."""
        return self._enrollment_resp.futureShowOnPortal

    @property
    def calendar_id(self) -> int:
        """Property Definition."""
        return self._enrollment_resp.calendarID

    @property
    def calendar_name(self) -> str:
        """Property Definition."""
        return self._enrollment_resp.calendarName

    @property
    def calendar_start_date(self) -> str:
        """Property Definition."""
        return self._enrollment_resp.calendarStartDate

    @property
    def calendar_end_date(self) -> str:
        """Property Definition."""
        return self._enrollment_resp.calendarEndDate
