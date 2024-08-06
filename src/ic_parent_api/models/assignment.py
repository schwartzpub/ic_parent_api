"""Assignment Model Definition."""

from typing import Optional
from datetime import datetime
import dateutil.parser
from ic_parent_api.ic_api_client import AssignmentResponse
from ic_parent_api.base import DataModel

class Assignment(DataModel):
    """Assignment Model Definition."""

    def __init__(self, assignment_resp: AssignmentResponse):
        self._assignment_resp=assignment_resp
    
    @property
    def object_section_id(self) -> int:
        """Property Definition."""
        return self._assignment_resp.objectSectionID

    @property
    def parentobjectsectionid(self) -> Optional[int]:
        """Property Definition."""
        return self._assignment_resp.parentObjectSectionID

    @property
    def type(self) -> int:
        """Property Definition."""
        return self._assignment_resp.type

    @property
    def personid(self) -> int:
        """Property Definition."""
        return self._assignment_resp.personID

    @property
    def taskid(self) -> Optional[int]:
        """Property Definition."""
        return self._assignment_resp.taskID

    @property
    def groupactivityid(self) -> int:
        """Property Definition."""
        return self._assignment_resp.groupActivityID

    @property
    def termids(self) -> list[int]:
        """Property Definition."""
        return self._assignment_resp.termIDs

    @property
    def assignment_name(self) -> str:
        """Property Definition."""
        return self._assignment_resp.assignmentName

    @property
    def calendarid(self) -> int:
        """Property Definition."""
        return self._assignment_resp.calendarID

    @property
    def structureid(self) -> int:
        """Property Definition."""
        return self._assignment_resp.structureID

    @property
    def sectionid(self) -> int:
        """Property Definition."""
        return self._assignment_resp.sectionID

    @property
    def due_date(self) -> Optional[datetime]:
        """Property Definition."""
        try:
            return dateutil.parser.parse(self._assignment_resp.dueDate)
        except (TypeError, ValueError):
            return None

    @property
    def assigned_date(self) -> str:
        """Property Definition."""
        return self._assignment_resp.assignedDate

    @property
    def modified_date(self) -> Optional[str]:
        """Property Definition."""
        return self._assignment_resp.modifiedDate

    @property
    def course_name(self) -> str:
        """Property Definition."""
        return self._assignment_resp.courseName

    @property
    def active(self) -> bool:
        """Property Definition."""
        return self._assignment_resp.active

    @property
    def scoringtype(self) -> Optional[str]:
        """Property Definition."""
        return self._assignment_resp.scoringType

    @property
    def score(self) -> Optional[str]:
        """Property Definition."""
        return self._assignment_resp.score

    @property
    def scorepoints(self) -> Optional[str]:
        """Property Definition."""
        return self._assignment_resp.scorePoints

    @property
    def scorepercentage(self) -> Optional[str]:
        """Property Definition."""
        return self._assignment_resp.scorePercentage

    @property
    def totalpoints(self) -> Optional[float]:
        """Property Definition."""
        return self._assignment_resp.totalPoints

    @property
    def comments(self) -> Optional[str]:
        """Property Definition."""
        return self._assignment_resp.comments

    @property
    def feedback(self) -> Optional[str]:
        """Property Definition."""
        return self._assignment_resp.feedback

    @property
    def late(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.late

    @property
    def missing(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.missing

    @property
    def cheated(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.cheated

    @property
    def dropped(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.dropped

    @property
    def incomplete(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.incomplete

    @property
    def turnedin(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.turnedIn

    @property
    def wysiwygsubmission(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.wysiwygSubmission

    @property
    def upload(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.upload

    @property
    def drivesubmission(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.driveSubmission

    @property
    def multiplier(self) -> Optional[float]:
        """Property Definition."""
        return self._assignment_resp.multiplier

    @property
    def hasstudenthtml(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasStudentHTML

    @property
    def hasteacherhtml(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasTeacherHTML

    @property
    def hasquiz(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasQuiz

    @property
    def haslti(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasLTI

    @property
    def hasltiacceptsscores(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasLTIAcceptsScores

    @property
    def hasfile(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasFile

    @property
    def hasexternalfile(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasExternalFile

    @property
    def hassubmission(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasSubmission

    @property
    def hasdiscussion(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasDiscussion

    @property
    def hasrubric(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.hasRubric

    @property
    def notgraded(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.notGraded

    @property
    def isvalidrubric(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.isValidRubric

    @property
    def isvalidmark(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.isValidMark

    @property
    def includecampuslearning(self) -> Optional[bool]:
        """Property Definition."""
        return self._assignment_resp.includeCampusLearning
