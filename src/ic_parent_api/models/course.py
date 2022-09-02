"""Course Model Definition."""
from ic_parent_api.base import DataModel
from ic_parent_api.models.placement import Placement
from ic_parent_api.ic_api_client import CourseResponse


class Course(DataModel):
    """Course Model Definition."""
    def __init__(self, course_resp: CourseResponse):
        self._id = course_resp.id
        self._rosterid = course_resp.rosterID
        self._personid = course_resp.personID
        self._structureid = course_resp.structureID
        self._calendarid = course_resp.calendarID
        self._schoolid = course_resp.schoolID
        self._courseid = course_resp.courseID
        self._sectionid = course_resp.sectionID
        self._coursename = course_resp.courseName
        self._coursenumber = course_resp.courseNumber
        self._isresponsive = course_resp.isResponsive
        self._sectionnumber = course_resp.sectionNumber
        self._endyear = course_resp.endYear
        self._schoolname = course_resp.schoolName
        self._trialid = course_resp.trialID
        self._trialactive = course_resp.trialActive
        self._roomname = course_resp.roomName
        self._teacherdisplay = course_resp.teacherDisplay
        self._hidestandardsonportal = course_resp.hideStandardsOnPortal
        self._sectionplacements = course_resp.sectionPlacements

    @property
    def id(self) -> str:
        """Property Definition."""
        return self._id

    @property
    def rosterid(self) -> int:
        """Property Definition."""
        return self._rosterid

    @property
    def personid(self) -> int:
        """Property Definition."""
        return self._personid

    @property
    def structureid(self) -> int:
        """Property Definition."""
        return self._structureid

    @property
    def calendarid(self) -> int:
        """Property Definition."""
        return self._calendarid

    @property
    def schoolid(self) -> int:
        """Property Definition."""
        return self._schoolid

    @property
    def coursename(self) -> str:
        """Property Definition."""
        return self._coursename

    @property
    def coursenumber(self) -> str:
        """Property Definition."""
        return self._coursenumber

    @property
    def isresponsive(self) -> bool:
        """Property Definition."""
        return self._isresponsive

    @property
    def sectionnumber(self) -> str:
        """Property Definition."""
        return self._sectionnumber

    @property
    def endyear(self) -> str:
        """Property Definition."""
        return self._endyear

    @property
    def schoolname(self) -> str:
        """Property Definition."""
        return self._schoolname

    @property
    def trialid(self) -> int:
        """Property Definition."""
        return self._trialid

    @property
    def trialactive(self) -> bool:
        """Property Definition."""
        return self._trialactive

    @property
    def roomname(self) -> str:
        """Property Definition."""
        return self._roomname

    @property
    def teacherdisplay(self) -> str:
        """Property Definition."""
        return self._teacherdisplay

    @property
    def hidestandardsonportal(self) -> bool:
        """Property Definition."""
        return self._hidestandardsonportal

    @property
    def sectionplacements(self) -> list[Placement]:
        """Property Definition."""
        return [Placement(placement) for placement in self._sectionplacements]
