"""Base Infinite Campus Class."""

import logging

from .models.student import Student
from .models.course import Course
from .models.assignment import Assignment
from .models.term import Term
from .ic_api_client import InfiniteCampusApiClient
from .ic_user import InfiniteCampusUser as User

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class InfiniteCampus:
    """Define InfiniteCampus Class."""

    def __init__(
        self,
        base_url,
        user: User,
        debug=False,
    ):
        self._api_client = InfiniteCampusApiClient(
            base_url, user, debug
        )

        if debug:
            _LOGGER.setLevel(logging.DEBUG)

    async def authenticate(self, session) -> bool:
        """Authenticate with Infinite Campus."""
        auth_resp = await self._api_client.authenticate(session)
        return auth_resp

    async def students(self) -> list[Student]:
        """Get Students."""
        students_resp = await self._api_client.get_students()
        students = [Student(response) for response in students_resp]
        return students

    async def courses(self, student_id) -> list[Course]:
        """Get Courses: must supply student id."""
        courses_resp = await self._api_client.get_courses(student_id)
        courses = [Course(response) for response in courses_resp]
        return courses

    async def assignments(self, student_id) -> list[Assignment]:
        """Get Assignments: must supply student id."""
        assignments_resp = await self._api_client.get_assignments(student_id)
        assignments = [Assignment(response) for response in assignments_resp]
        return assignments

    async def terms(self, structure_id) -> list[Term]:
        """Get Terms."""
        terms_resp = await self._api_client.get_terms(structure_id)
        terms = [Term(response) for response in terms_resp]
        return terms
