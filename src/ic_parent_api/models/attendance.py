"""Attendance Model Definition."""
from typing import Optional
from ic_parent_api.base import DataModel
from ic_parent_api.models.base import AttendanceResponse


class AttendanceCourse(DataModel):
    """Attendance Course Model Definition."""
    def __init__(self, course_data: dict):
        self._courseid = course_data.get('courseID')
        self._coursename = course_data.get('courseName')
        self._sectionid = course_data.get('sectionID')
        self._totalabsent = course_data.get('totalAbsent', 0) or 0
        self._totaltardy = course_data.get('totalTardy', 0) or 0
        self._totalexcused = course_data.get('totalExcused', 0) or 0
        self._totalunexcused = course_data.get('totalUnexcused', 0) or 0

    @property
    def courseid(self) -> Optional[int]:
        """Property Definition."""
        return self._courseid

    @property
    def coursename(self) -> Optional[str]:
        """Property Definition."""
        return self._coursename

    @property
    def sectionid(self) -> Optional[int]:
        """Property Definition."""
        return self._sectionid

    @property
    def totalabsent(self) -> float:
        """Total absences for this course."""
        return self._totalabsent

    @property
    def totaltardy(self) -> float:
        """Total tardies for this course."""
        return self._totaltardy

    @property
    def totalexcused(self) -> float:
        """Total excused absences for this course."""
        return self._totalexcused

    @property
    def totalunexcused(self) -> float:
        """Total unexcused absences for this course."""
        return self._totalunexcused


class AttendanceTerm(DataModel):
    """Attendance Term Model Definition."""
    def __init__(self, term_data: dict):
        self._termid = term_data.get('termID')
        self._termname = term_data.get('termName')
        self._courses = term_data.get('courses', [])

    @property
    def termid(self) -> Optional[int]:
        """Property Definition."""
        return self._termid

    @property
    def termname(self) -> Optional[str]:
        """Property Definition."""
        return self._termname

    @property
    def courses(self) -> list[AttendanceCourse]:
        """Property Definition."""
        return [AttendanceCourse(course) for course in self._courses]

    @property
    def totalabsent(self) -> float:
        """Total absences across all courses for this term."""
        return sum(course.totalabsent for course in self.courses)

    @property
    def totaltardy(self) -> float:
        """Total tardies across all courses for this term."""
        return sum(course.totaltardy for course in self.courses)


class Attendance(DataModel):
    """Attendance Model Definition."""
    def __init__(self, attendance_resp: AttendanceResponse):
        self._terms = attendance_resp.terms or []

    @property
    def terms(self) -> list[AttendanceTerm]:
        """Property Definition."""
        return [AttendanceTerm(term.model_dump()) for term in self._terms]
