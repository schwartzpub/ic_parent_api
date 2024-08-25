"""Infinite Campus API Client."""

import logging
from urllib.parse import urljoin

import aiohttp

from .ic_user import InfiniteCampusUser as User
from .errors import InfiniteCampusError
from .models.base import (
    StudentResponse,
    CourseResponse,
    AssignmentResponse,
    TermResponse,
    ScheduleDayResponse,
)

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


def _enable_debug_logging():
    _LOGGER.setLevel(logging.DEBUG)


class InfiniteCampusApiClient:
    """Infinite Campus Parent API Client."""

    def __init__(
        self,
        base_url: str,
        user: User,
        debug=False,
    ):
        if debug:
            _enable_debug_logging()

        self._base_url = base_url

        _LOGGER.debug("base url: %s", self._base_url)

        self._username = user.username
        self._secret = user.password
        self._district = user.district
        self._headers = {"Accept": "application/json"}

    async def authenticate(self, session) -> bool:
        """Test if we can authenticate with the district."""
        try:
            request_url = urljoin(
                self._base_url,
                (
                    f"/campus/verify.jsp?nonBrowser=true"
                    f"&username={self._username}"
                    f"&password={self._secret}"
                    f"&appName={self._district}"
                    "&portalLoginPage=parents"
                ),
            )
            async with session.post(request_url) as auth_response:
                response = auth_response
                response_text = await response.text()
                if response.status == 200 and "password-error" not in response_text:
                    return True
                raise InfiniteCampusError(400, "Bad Credentials")
        except Exception as error:
            raise InfiniteCampusError(400, error) from InfiniteCampusError

    async def _get_request(self, end_url: str):
        """Perform GET request to API endpoint."""
        request_url = urljoin(self._base_url, end_url)
        async with aiohttp.ClientSession() as session:
            authenticated = await self.authenticate(session)
            if authenticated:
                async with session.get(f"{request_url}", headers=self._headers) as resp:
                    response = resp
                    response_text = await resp.text()
                    response_json = await resp.json()
                    if response.status >= 400:
                        raise InfiniteCampusError(response.status, response_text)
                    return response_json
            raise InfiniteCampusError(400, "Bad Credentials")

    async def get_students(self) -> list[StudentResponse]:
        """Get Infinite Campus Students."""
        parsed_response = await self._get_request("/campus/api/portal/students")
        schedule_days_list: list[ScheduleDayResponse] = []
        if parsed_response:
            student_resp: list[StudentResponse] = [
                StudentResponse(**resp) for resp in parsed_response
            ]
            for student in student_resp:
                for enrollment in student.enrollments:
                    schedule_days = await self.get_schedule_days(enrollment.calendarID)
                    schedule_days_list.extend(schedule_days)
                student.scheduleDays = schedule_days_list
            return student_resp
        return []

    async def get_courses(self, student_id: int) -> list[CourseResponse]:
        """Get Infinite Campus Courses."""
        parsed_response = await self._get_request(
            f"/campus/resources/portal/roster?&personID={student_id}"
        )
        if parsed_response:
            return [CourseResponse(**resp) for resp in parsed_response]
        return []

    async def get_assignments(self, student_id: int) -> list[AssignmentResponse]:
        """Get Infinite Campus Courses."""
        parsed_response = await self._get_request(
            f"/campus/api/portal/assignment/listView?&personID={student_id}"
        )
        if parsed_response:
            return [AssignmentResponse(**resp) for resp in parsed_response]
        return []

    async def get_terms(self, structure_id) -> list[TermResponse]:
        """Get Infinite Campus Courses."""
        parsed_response = await self._get_request(
            f"/campus/resources/term?structureID={structure_id}"
        )
        if parsed_response:
            return [TermResponse(**resp) for resp in parsed_response]
        return []

    async def get_schedule_days(self, calendar_id: int) -> list[ScheduleDayResponse]:
        """Get Infinite Campus Courses."""
        parsed_response = await self._get_request(
            f"/campus/resources/calendar/instructionalDay?calendarID={calendar_id}"
        )
        if parsed_response:
            return [ScheduleDayResponse(**resp) for resp in parsed_response]
        return []
