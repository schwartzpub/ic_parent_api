"""Enrollment Model Definition."""
from ic_parent_api.base import DataModel
from ic_parent_api.ic_api_client import EnrollmentResponse


class Enrollment(DataModel):
    """Enrollment Model Definition."""
    def __init__(self, enrollment_resp: EnrollmentResponse):
        self._enrollmentid = enrollment_resp.enrollmentID
        self._personid = enrollment_resp.personID
        self._calendarid = enrollment_resp.calendarID
        self._structureid = enrollment_resp.structureID
        self._districtid = enrollment_resp.districtID
        self._endyear = enrollment_resp.endYear
        self._servicetype = enrollment_resp.serviceType
        self._startdate = enrollment_resp.startDate
        self._enddate = enrollment_resp.endDate
        self._grade = enrollment_resp.grade
        self._structurename = enrollment_resp.structureName
        self._calendarname = enrollment_resp.calendarName
        self._schoolid = enrollment_resp.schoolID
        self._schoolname = enrollment_resp.schoolName
        self._showonportal = enrollment_resp.showOnPortal
        self._futureshowonportal = enrollment_resp.futureShowOnPortal
        self._calendarstartdate = enrollment_resp.calendarStartDate
        self._calendarenddate = enrollment_resp.calendarEndDate

    @property
    def enrollmentid(self) -> int:
        """Property Definition."""
        return self._enrollmentid

    @property
    def personid(self) -> int:
        """Property Definition."""
        return self._personid

    @property
    def calendarid(self) -> int:
        """Property Definition."""
        return self._calendarid

    @property
    def structureid(self) -> int:
        """Property Definition."""
        return self._structureid

    @property
    def districtid(self) -> int:
        """Property Definition."""
        return self._districtid

    @property
    def endyear(self) -> int:
        """Property Definition."""
        return self._endyear

    @property
    def servicetype(self) -> str:
        """Property Definition."""
        return self._servicetype

    @property
    def startdate(self) -> str:
        """Property Definition."""
        return self._startdate

    @property
    def enddate(self) -> str:
        """Property Definition."""
        return self._enddate

    @property
    def grade(self) -> str:
        """Property Definition."""
        return self._grade

    @property
    def structurename(self) -> str:
        """Property Definition."""
        return self._structurename

    @property
    def calendarname(self) -> str:
        """Property Definition."""
        return self._calendarname

    @property
    def schoolid(self) -> int:
        """Property Definition."""
        return self._schoolid

    @property
    def schoolname(self) -> str:
        """Property Definition."""
        return self._schoolname

    @property
    def showonportal(self) -> bool:
        """Property Definition."""
        return self._showonportal

    @property
    def futureshowonportal(self) -> bool:
        """Property Definition."""
        return self._futureshowonportal

    @property
    def calendarstartdate(self) -> str:
        """Property Definition."""
        return self._calendarstartdate

    @property
    def calendarenddate(self) -> str:
        """Property Definition."""
        return self._calendarenddate
