"""Infinite Campus Error Returns.

Adapted from pygrocy (https://github.com/SebRut/pygrocy).
"""


class InfiniteCampusError(Exception):
    def __init__(self, response: int, text: str):
        self._status = response
        self._text = text

        if len(self._text) > 0:
            self._message = self._text
        else:
            self._message = None

    @property
    def status(self) -> int:
        return self._status

    @property
    def message(self) -> str:
        return self._message

    @property
    def is_client_error(self) -> bool:
        return 400 <= self.status < 500

    @property
    def is_server_error(self) -> bool:
        return self.status >= 500
