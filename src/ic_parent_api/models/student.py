"""Student Model Definition."""
from ic_parent_api.base import DataModel
from ic_parent_api.models.scheduleday import ScheduleDay
from ic_parent_api.models.enrollment import Enrollment
from ic_parent_api.ic_api_client import StudentResponse


class Student(DataModel):
    """Student Model Definition."""
    def __init__(self, student_resp: StudentResponse):
        self._personid = student_resp.personID
        self._guardian = student_resp.guardian
        self._firstname = student_resp.firstName
        self._lastname = student_resp.lastName
        self._middlename = student_resp.middleName
        self._suffix = student_resp.suffix
        self._alias = student_resp.alias
        self._studentnumber = student_resp.studentNumber
        self._hasportalenrollment = student_resp.hasPortalEnrollment
        self._enrollments = student_resp.enrollments
        self._futureenrollments = student_resp.futureEnrollments
        self._scheduledays = student_resp.scheduleDays

    @property
    def personid(self) -> int:
        """Property Definition."""
        return self._personid

    @property
    def guardian(self) -> bool:
        """Property Definition."""
        return self._guardian

    @property
    def firstname(self) -> str:
        """Property Definition."""
        return self._firstname

    @property
    def lastname(self) -> str:
        """Property Definition."""
        return self._lastname

    @property
    def middlename(self) -> str:
        """Property Definition."""
        return self._middlename

    @property
    def suffix(self) -> str:
        """Property Definition."""
        return self._suffix

    @property
    def alias(self) -> str:
        """Property Definition."""
        return self._alias

    @property
    def studentnumber(self) -> int:
        """Property Definition."""
        return self._studentnumber

    @property
    def hasportalenrollment(self) -> bool:
        """Property Definition."""
        return self._hasportalenrollment

    @property
    def enrollments(self) -> list[Enrollment]:
        """Property Definition."""
        return [Enrollment(enrollment) for enrollment in self._enrollments]

    @property
    def futureenrollments(self) -> list[Enrollment]:
        """Property Definition."""
        return [Enrollment(enrollment) for enrollment in self._futureenrollments]

    @property
    def scheduledays(self) -> list[ScheduleDay]:
        """Property Definition."""
        return [ScheduleDay(scheduleday) for scheduleday in self._scheduledays]
