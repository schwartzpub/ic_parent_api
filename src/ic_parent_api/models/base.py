"""Base Model Definition."""
from typing import Optional
from pydantic import BaseModel,Field

class StudentResponse(BaseModel):
    """Student Response Definition."""
    personID: int
    guardian: bool
    firstName: str
    lastName: str
    middleName: str
    suffix: Optional[str]
    alias: Optional[str]
    studentNumber: int
    hasPortalEnrollment: bool
    enrollments: list[dict]
    futureEnrollments: list[dict]
    scheduleDays: Optional[list[dict]]

class CourseResponse(BaseModel):
    """Course Response Definition."""
    class Config:
        exclude = ['_model','_hashCode']
    id: str = Field(alias='_id')
    rosterID: int
    personID: int
    structureID: int
    calendarID: int
    schoolID: int
    courseID: int
    sectionID: int
    courseName: str
    courseNumber: str
    isResponsive: bool
    sectionNumber: str
    endYear: int
    schoolName: str
    trialID: int
    trialActive: bool
    roomName: Optional[str]
    teacherDisplay: str
    hideStandardsOnPortal: bool
    sectionPlacements: list[dict]

class PlacementResponse(BaseModel):
    """Course Placement Response Definition."""
    class Config:
        exclude = ['_model','_hashCode']
    id: str = Field(alias='_id')
    sectionID: int
    termID: int
    termName: str
    termSeq: int
    periodID: int
    trialID: int
    periodSequence: int
    term: dict
    periodScheduleID: int
    startTime: str
    endTIme: str
    periodName: str
    periodScheduleName: str
    teacherDisplay: str
    periodScheduleSequence: int
    structureID: int
    courseID: int
    courseNumber: str
    sectionNumber: int
    courseName: str
    termScheduleID: int
    startDate: str
    endDate: str
    roomID: int
    roomName: str
    unitAttendance: bool
    attendance: bool
    isResponsive: bool

class AssignmentResponse(BaseModel):
    """Assignment Response Definition."""
    objectSectionID: int
    parentObjectSectionID: Optional[int]
    type: int
    personID: int
    taskID: Optional[int]
    groupActivityID: int
    termIDs: list[int]
    assignmentName: str
    calendarID: int
    structureID: int
    sectionID: int
    dueDate: str
    assignedDate: str
    modifiedDate: Optional[str]
    courseName: str
    active: bool
    scoringType: str
    score: Optional[str]
    scorePoints: Optional[str]
    scorePercentage: Optional[str]
    totalPoints: Optional[float]
    comments: Optional[str]
    feedback: Optional[str]
    late: Optional[bool]
    missing: Optional[bool]
    cheated: Optional[bool]
    dropped: Optional[bool]
    incomplete: Optional[bool]
    turnedIn: Optional[bool]
    wysiwygSubmission: Optional[bool]
    upload: Optional[bool]
    driveSubmission: Optional[bool]
    multiplier: Optional[float]
    hasStudentHTML: Optional[bool]
    hasTeacherHTML: Optional[bool]
    hasQuiz: Optional[bool]
    hasLTI: Optional[bool]
    hasLTIAcceptsScores: Optional[bool]
    hasFile: Optional[bool]
    hasExternalFile: Optional[bool]
    hasSubmission: Optional[bool]
    hasDiscussion: Optional[bool]
    hasRubric: Optional[bool]
    notGraded: Optional[bool]
    isValidRubric: Optional[bool]
    isValidMark: Optional[bool]
    includeCampusLearning: Optional[bool]

class ScheduleDayResponse(BaseModel):
    """ScheduleDay Response Definition."""
    class Config:
        exclude = ['_model','_hashCode']
    id:  str = Field(alias='_id')
    dayID: int
    calendarID: int
    structureID: int
    periodScheduleID: int
    date: str
    requiresAttendance: bool
    isSchoolDay: bool
    duration: int
    trialID: int

class TermResponse(BaseModel):
    """Term Response Definition."""
    class Config:
        exclude = ['_model','_hashCode']
    id: str = Field(alias='_id')
    termID: int
    termScheduleID: int
    seq: int
    startDate: str
    endDate: str
    termName: str
    structureID: int
    isPrimary: bool
    termScheduleName: str
    calendarID: int
    scheduleStructureName: str
