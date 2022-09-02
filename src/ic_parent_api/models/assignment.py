"""Assignment Model Definition."""
from ic_parent_api.base import DataModel
from ic_parent_api.ic_api_client import AssignmentResponse


class Assignment(DataModel):
    """Assignment Model Definition."""
    def __init__(self, assignment_resp: AssignmentResponse):
        self._objectsectionid = assignment_resp.objectSectionID
        self._parentobjectsectionid = assignment_resp.parentObjectSectionID
        self._type = assignment_resp.type
        self._personid = assignment_resp.personID
        self._taskid = assignment_resp.taskID
        self._groupactivityid = assignment_resp.groupActivityID
        self._termids = assignment_resp.termIDs
        self._assignmentname = assignment_resp.assignmentName
        self._calendarid = assignment_resp.calendarID
        self._structureid = assignment_resp.structureID
        self._sectionid = assignment_resp.sectionID
        self._duedate = assignment_resp.dueDate
        self._assigneddate = assignment_resp.assignedDate
        self._modifieddate = assignment_resp.modifiedDate
        self._coursename = assignment_resp.courseName
        self._active = assignment_resp.active
        self._scoringtype = assignment_resp.scoringType
        self._score = assignment_resp.score
        self._scorepoints = assignment_resp.scorePoints
        self._scorepercentage = assignment_resp.scorePercentage
        self._totalpoints = assignment_resp.totalPoints
        self._comments = assignment_resp.comments
        self._feedback = assignment_resp.feedback
        self._late = assignment_resp.late
        self._missing = assignment_resp.missing
        self._cheated = assignment_resp.cheated
        self._dropped = assignment_resp.dropped
        self._incomplete = assignment_resp.incomplete
        self._turnedin = assignment_resp.turnedIn
        self._wysiwygsubmission = assignment_resp.wysiwygSubmission
        self._upload = assignment_resp.upload
        self._drivesubmission = assignment_resp.driveSubmission
        self._multiplier = assignment_resp.multiplier
        self._hasstudenthtml = assignment_resp.hasStudentHTML
        self._hasteacherhtml = assignment_resp.hasTeacherHTML
        self._hasquiz = assignment_resp.hasQuiz
        self._haslti = assignment_resp.hasLTI
        self._hasltiacceptsscores = assignment_resp.hasLTIAcceptsScores
        self._hasfile = assignment_resp.hasFile
        self._hasexternalfile = assignment_resp.hasExternalFile
        self._hassubmission = assignment_resp.hasSubmission
        self._hasdiscussion = assignment_resp.hasDiscussion
        self._hasrubric = assignment_resp.hasRubric
        self._notgraded = assignment_resp.notGraded
        self._isvalidrubric = assignment_resp.isValidRubric
        self._isvalidmark = assignment_resp.isValidMark
        self._includecampuslearning = assignment_resp.includeCampusLearning

    @property
    def objectsectionid(self) -> int:
        """Property Definition."""
        return self._objectsectionid

    @property
    def parentobjectsectionid(self) -> int:
        """Property Definition."""
        return self._parentobjectsectionid

    @property
    def type(self) -> int:
        """Property Definition."""
        return self._type

    @property
    def personid(self) -> int:
        """Property Definition."""
        return self._personid

    @property
    def taskid(self) -> int:
        """Property Definition."""
        return self._taskid

    @property
    def groupactivityid(self) -> int:
        """Property Definition."""
        return self._groupactivityid

    @property
    def termids(self) -> list[int]:
        """Property Definition."""
        return self._termids

    @property
    def assignmentname(self) -> str:
        """Property Definition."""
        return self._assignmentname

    @property
    def calendarid(self) -> int:
        """Property Definition."""
        return self._calendarid

    @property
    def structureid(self) -> int:
        """Property Definition."""
        return self._structureid

    @property
    def sectionid(self) -> int:
        """Property Definition."""
        return self._sectionid

    @property
    def duedate(self) -> str:
        """Property Definition."""
        return self._duedate

    @property
    def assigneddate(self) -> str:
        """Property Definition."""
        return self._assigneddate

    @property
    def modifieddate(self) -> str:
        """Property Definition."""
        return self._modifieddate

    @property
    def coursename(self) -> str:
        """Property Definition."""
        return self._coursename

    @property
    def active(self) -> bool:
        """Property Definition."""
        return self._active

    @property
    def scoringtype(self) -> str:
        """Property Definition."""
        return self._scoringtype

    @property
    def score(self) -> str:
        """Property Definition."""
        return self._score

    @property
    def scorepoints(self) -> str:
        """Property Definition."""
        return self._scorepoints

    @property
    def scorepercentage(self) -> str:
        """Property Definition."""
        return self._scorepercentage

    @property
    def totalpoints(self) -> float:
        """Property Definition."""
        return self._totalpoints

    @property
    def comments(self) -> str:
        """Property Definition."""
        return self._comments

    @property
    def feedback(self) -> str:
        """Property Definition."""
        return self._feedback

    @property
    def late(self) -> bool:
        """Property Definition."""
        return self._late

    @property
    def missing(self) -> bool:
        """Property Definition."""
        return self._missing

    @property
    def cheated(self) -> bool:
        """Property Definition."""
        return self._cheated

    @property
    def dropped(self) -> bool:
        """Property Definition."""
        return self._dropped

    @property
    def incomplete(self) -> bool:
        """Property Definition."""
        return self._incomplete

    @property
    def turnedin(self) -> bool:
        """Property Definition."""
        return self._turnedin

    @property
    def wysiwygsubmission(self) -> bool:
        """Property Definition."""
        return self._wysiwygsubmission

    @property
    def upload(self) -> bool:
        """Property Definition."""
        return self._upload

    @property
    def drivesubmission(self) -> bool:
        """Property Definition."""
        return self._drivesubmission

    @property
    def multiplier(self) -> bool:
        """Property Definition."""
        return self._multiplier

    @property
    def hasstudenthtml(self) -> bool:
        """Property Definition."""
        return self._hasstudenthtml

    @property
    def hasteacherhtml(self) -> bool:
        """Property Definition."""
        return self._hasteacherhtml

    @property
    def hasquiz(self) -> bool:
        """Property Definition."""
        return self._hasquiz

    @property
    def haslti(self) -> bool:
        """Property Definition."""
        return self._haslti

    @property
    def hasltiacceptsscores(self) -> bool:
        """Property Definition."""
        return self._hasltiacceptsscores

    @property
    def hasfile(self) -> bool:
        """Property Definition."""
        return self._hasfile

    @property
    def hasexternalfile(self) -> bool:
        """Property Definition."""
        return self._hasexternalfile

    @property
    def hassubmission(self) -> bool:
        """Property Definition."""
        return self._hassubmission

    @property
    def hasdiscussion(self) -> bool:
        """Property Definition."""
        return self._hasdiscussion

    @property
    def hasrubric(self) -> bool:
        """Property Definition."""
        return self._hasrubric

    @property
    def notgraded(self) -> bool:
        """Property Definition."""
        return self._notgraded

    @property
    def isvalidrubric(self) -> bool:
        """Property Definition."""
        return self._isvalidrubric

    @property
    def isvalidmark(self) -> bool:
        """Property Definition."""
        return self._isvalidmark

    @property
    def includecampuslearning(self) -> bool:
        """Property Definition."""
        return self._includecampuslearning
