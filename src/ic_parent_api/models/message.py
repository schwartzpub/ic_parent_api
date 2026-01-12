"""Message Model Definition."""
import re
import html
from typing import Optional
from ic_parent_api.base import DataModel
from ic_parent_api.models.base import MessageResponse, MessageDetailResponse


class Message(DataModel):
    """Message Model Definition."""
    def __init__(self, message_resp: MessageResponse):
        self._messageid = message_resp.messageID
        self._actionrequired = message_resp.actionRequired
        self._postedtimestamp = message_resp.postedTimestamp
        self._date = message_resp.date
        self._name = message_resp.name
        self._duedate = message_resp.dueDate
        self._newmessage = message_resp.newMessage
        self._personid = message_resp.personID
        self._process = message_resp.process
        self._url = message_resp.url
        self._sectionid = message_resp.sectionID
        self._schoolid = message_resp.schoolID
        self._calendarid = message_resp.calendarID
        self._sender = message_resp.sender
        self._studentid = message_resp.studentID
        self._studentname = message_resp.studentName
        self._courseid = message_resp.courseID
        self._coursename = message_resp.courseName
        self._messagetype = message_resp.messageType

    @property
    def messageid(self) -> Optional[int]:
        """Property Definition."""
        return self._messageid

    @property
    def actionrequired(self) -> Optional[bool]:
        """Property Definition."""
        return self._actionrequired

    @property
    def postedtimestamp(self) -> Optional[str]:
        """Property Definition."""
        return self._postedtimestamp

    @property
    def date(self) -> Optional[str]:
        """Property Definition."""
        return self._date

    @property
    def name(self) -> Optional[str]:
        """Message subject/name."""
        return self._name

    @property
    def subject(self) -> Optional[str]:
        """Alias for name (message subject)."""
        return self._name

    @property
    def duedate(self) -> Optional[str]:
        """Property Definition."""
        return self._duedate

    @property
    def newmessage(self) -> Optional[bool]:
        """Whether this is an unread message."""
        return self._newmessage

    @property
    def personid(self) -> Optional[int]:
        """Property Definition."""
        return self._personid

    @property
    def process(self) -> Optional[str]:
        """Property Definition."""
        return self._process

    @property
    def url(self) -> Optional[str]:
        """URL to view message details."""
        return self._url

    @property
    def sectionid(self) -> Optional[int]:
        """Property Definition."""
        return self._sectionid

    @property
    def schoolid(self) -> Optional[int]:
        """Property Definition."""
        return self._schoolid

    @property
    def calendarid(self) -> Optional[int]:
        """Property Definition."""
        return self._calendarid

    @property
    def sender(self) -> Optional[str]:
        """Property Definition."""
        return self._sender

    @property
    def studentid(self) -> Optional[int]:
        """Property Definition."""
        return self._studentid

    @property
    def studentname(self) -> Optional[str]:
        """Property Definition."""
        return self._studentname

    @property
    def courseid(self) -> Optional[int]:
        """Property Definition."""
        return self._courseid

    @property
    def coursename(self) -> Optional[str]:
        """Property Definition."""
        return self._coursename

    @property
    def messagetype(self) -> Optional[str]:
        """Property Definition."""
        return self._messagetype

    def parse_url_ids(self) -> Optional[dict]:
        """Parse message IDs from URL for fetching full content."""
        if not self._url:
            return None
        match = re.search(
            r'messageID=(\d+)&messageRecipientID=(\d+)&processMessageID=(\d+)',
            self._url
        )
        if match:
            return {
                'message_id': match.group(1),
                'message_recipient_id': match.group(2),
                'process_message_id': match.group(3)
            }
        return None


class MessageDetail(DataModel):
    """Message Detail Model Definition (full message content)."""
    def __init__(self, detail_data: dict):
        # Navigate nested response structure
        data = detail_data.get('data', {})
        msg_view = data.get('MessageRecipientView', {})
        msg = msg_view.get('Message', {})

        self._messageid = msg.get('messageID')
        self._createdtimestamp = msg.get('createdTimeStamp')
        self._deliverytimestamp = msg.get('deliveryTimeStamp')
        self._senderid = msg.get('senderID')
        self._subject = msg.get('subject')
        self._body = msg.get('body')

    @property
    def messageid(self) -> Optional[str]:
        """Property Definition."""
        return self._messageid

    @property
    def createdtimestamp(self) -> Optional[str]:
        """Property Definition."""
        return self._createdtimestamp

    @property
    def deliverytimestamp(self) -> Optional[str]:
        """Property Definition."""
        return self._deliverytimestamp

    @property
    def senderid(self) -> Optional[str]:
        """Property Definition."""
        return self._senderid

    @property
    def subject(self) -> Optional[str]:
        """Property Definition."""
        return self._subject

    @property
    def body(self) -> Optional[str]:
        """Raw HTML body of the message."""
        return self._body

    @property
    def body_text(self) -> Optional[str]:
        """Clean plain text version of the message body."""
        if not self._body:
            return None
        # Remove style block content
        clean = re.sub(r'<style[^>]*>.*?</style>', '', self._body, flags=re.DOTALL)
        # Remove HTML tags
        clean = re.sub(r'<[^>]+>', ' ', clean)
        # Normalize whitespace
        clean = re.sub(r'\s+', ' ', clean).strip()
        # Unescape HTML entities
        clean = html.unescape(clean)
        # Remove XML declaration
        clean = re.sub(r'<\?xml[^>]+\?>', '', clean)
        return clean.strip()
