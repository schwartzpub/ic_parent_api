"""Base Infinite Campus Class."""
import logging

from .models.student import Student
from .models.course import Course
from .models.assignment import Assignment
from .models.term import Term
from .models.grade import Grade
from .models.attendance import Attendance
from .models.message import Message, MessageDetail
from .ic_api_client import InfiniteCampusApiClient

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class InfiniteCampus():
    """Define InfiniteCampus Class."""
    def __init__(
        self,
        base_url,
        username,
        secret,
        district,
        path: str = None,
        debug=False,
    ):
        self._api_client = InfiniteCampusApiClient(base_url, username, secret, district, path, debug)

        if debug:
            _LOGGER.setLevel(logging.DEBUG)

    async def authenticate(self, session) -> bool:
        """Authenticate with Infinite Campus."""
        authresp = await self._api_client.authenticate(session)
        return authresp

    async def students(self) -> list[Student]:
        """Get Students."""
        studentsresp = await self._api_client.get_students()
        students = [Student(response) for response in studentsresp]
        return students

    async def courses(self, student_id) -> list[Course]:
        """Get Courses: must supply student id."""
        coursesresp = await self._api_client.get_courses(student_id)
        courses = [Course(response) for response in coursesresp]
        return courses

    async def assignments(self, student_id) -> list[Assignment]:
        """Get Assignments: must supply student id."""
        assignmentsresp = await self._api_client.get_assignments(student_id)
        assignments = [Assignment(response) for response in assignmentsresp]
        return assignments

    async def terms(self) -> list[Term]:
        """Get Terms."""
        termsresp = await self._api_client.get_terms()
        terms = [Term(response) for response in termsresp]
        return terms

    async def grades(self, student_id: int) -> list[Grade]:
        """Get Grades: must supply student id (personID)."""
        gradesresp = await self._api_client.get_grades(student_id)
        grades = [Grade(response) for response in gradesresp]
        return grades

    async def attendance(self, enrollment_id: int, student_id: int) -> Attendance:
        """Get Attendance: must supply enrollment id and student id (personID)."""
        attendanceresp = await self._api_client.get_attendance(enrollment_id, student_id)
        return Attendance(attendanceresp)

    async def messages(self) -> list[Message]:
        """Get Inbox Messages."""
        messagesresp = await self._api_client.get_messages()
        messages = [Message(response) for response in messagesresp]
        return messages

    async def message_detail(self, message: Message) -> MessageDetail:
        """Get full message content: must supply a Message object."""
        ids = message.parse_url_ids()
        if not ids:
            return MessageDetail({})
        detail = await self._api_client.get_message_detail(
            ids['message_id'],
            ids['message_recipient_id'],
            ids['process_message_id']
        )
        return MessageDetail(detail)
