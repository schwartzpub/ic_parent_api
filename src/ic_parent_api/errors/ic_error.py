"""Infinite Campus Error Returns.

Adapted from pygrocy (https://github.com/SebRut/pygrocy).
"""


class InfiniteCampusError(Exception):
    """Errors for Infinite Campus returns"""

    def __init__(self, response: int, text: str):
        self._status = response
        self._text = text

        if len(self._text) > 0:
            self._message = self._text
        else:
            self._message = ""

    @property
    def status(self) -> int:
        """HTTP status"""
        return self._status

    @property
    def message(self) -> str:
        """Message with error"""
        return self._message

    @property
    def is_client_error(self) -> bool:
        """Is a client error"""
        return 400 <= self.status < 500

    @property
    def is_server_error(self) -> bool:
        """Is a sever side error"""
        return self.status >= 500
