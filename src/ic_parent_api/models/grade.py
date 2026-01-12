"""Grade Model Definition."""
from typing import Optional
from ic_parent_api.base import DataModel
from ic_parent_api.models.base import GradeResponse, GradeTermResponse, GradeCourseResponse


class GradingTask(DataModel):
    """Grading Task Model Definition."""
    def __init__(self, task_data: dict):
        self._personid = task_data.get('personID')
        self._courseid = task_data.get('courseID')
        self._coursename = task_data.get('courseName')
        self._taskid = task_data.get('taskID')
        self._taskname = task_data.get('taskName')
        self._termid = task_data.get('termID')
        self._score = task_data.get('score')
        self._progressscore = task_data.get('progressScore')
        self._progresspercent = task_data.get('progressPercent')
        self._scoreid = task_data.get('scoreID')

    @property
    def personid(self) -> Optional[int]:
        """Property Definition."""
        return self._personid

    @property
    def courseid(self) -> Optional[int]:
        """Property Definition."""
        return self._courseid

    @property
    def coursename(self) -> Optional[str]:
        """Property Definition."""
        return self._coursename

    @property
    def taskid(self) -> Optional[int]:
        """Property Definition."""
        return self._taskid

    @property
    def taskname(self) -> Optional[str]:
        """Property Definition."""
        return self._taskname

    @property
    def termid(self) -> Optional[int]:
        """Property Definition."""
        return self._termid

    @property
    def score(self) -> Optional[str]:
        """Posted grade (e.g., 'A', 'B+')."""
        return self._score

    @property
    def progressscore(self) -> Optional[str]:
        """In-progress grade."""
        return self._progressscore

    @property
    def progresspercent(self) -> Optional[float]:
        """In-progress percentage."""
        return self._progresspercent

    @property
    def scoreid(self) -> Optional[int]:
        """Property Definition."""
        return self._scoreid

    @property
    def grade(self) -> Optional[str]:
        """Get the best available grade (posted or in-progress)."""
        return self._score or self._progressscore


class GradeCourse(DataModel):
    """Grade Course Model Definition."""
    def __init__(self, course_data: dict):
        self._courseid = course_data.get('courseID')
        self._coursename = course_data.get('courseName')
        self._coursenumber = course_data.get('courseNumber')
        self._sectionid = course_data.get('sectionID')
        self._teacherdisplay = course_data.get('teacherDisplay')
        self._gradingtasks = course_data.get('gradingTasks', [])

    @property
    def courseid(self) -> Optional[int]:
        """Property Definition."""
        return self._courseid

    @property
    def coursename(self) -> Optional[str]:
        """Property Definition."""
        return self._coursename

    @property
    def coursenumber(self) -> Optional[str]:
        """Property Definition."""
        return self._coursenumber

    @property
    def sectionid(self) -> Optional[int]:
        """Property Definition."""
        return self._sectionid

    @property
    def teacherdisplay(self) -> Optional[str]:
        """Property Definition."""
        return self._teacherdisplay

    @property
    def gradingtasks(self) -> list[GradingTask]:
        """Property Definition."""
        return [GradingTask(task) for task in self._gradingtasks]

    @property
    def grade(self) -> Optional[str]:
        """Get the primary grade for this course."""
        for task in self.gradingtasks:
            if task.grade:
                return task.grade
        return None


class GradeTerm(DataModel):
    """Grade Term Model Definition."""
    def __init__(self, term_data: dict):
        self._termid = term_data.get('termID')
        self._termname = term_data.get('termName')
        self._termseq = term_data.get('termSeq')
        self._startdate = term_data.get('startDate')
        self._enddate = term_data.get('endDate')
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
    def termseq(self) -> Optional[int]:
        """Property Definition."""
        return self._termseq

    @property
    def startdate(self) -> Optional[str]:
        """Property Definition."""
        return self._startdate

    @property
    def enddate(self) -> Optional[str]:
        """Property Definition."""
        return self._enddate

    @property
    def courses(self) -> list[GradeCourse]:
        """Property Definition."""
        return [GradeCourse(course) for course in self._courses]


class Grade(DataModel):
    """Grade Model Definition (enrollment level)."""
    def __init__(self, grade_resp: GradeResponse):
        self._enrollmentid = grade_resp.enrollmentID
        self._terms = grade_resp.terms or []

    @property
    def enrollmentid(self) -> Optional[int]:
        """Property Definition."""
        return self._enrollmentid

    @property
    def terms(self) -> list[GradeTerm]:
        """Property Definition."""
        return [GradeTerm(term.model_dump()) for term in self._terms]
