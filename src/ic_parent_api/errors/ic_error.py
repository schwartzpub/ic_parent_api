"""Infinite Campus Error Returns.

Adapted from pygrocy (https://github.com/SebRut/pygrocy).
"""
from aiohttp import ClientResponse

class InfiniteCampusError(Exception):
    def __init__(self, response: ClientResponse, text: str):
        self._status = response.status
        self._text = text

        if len(response.text) > 0:
            json = response.json()
            self._message = json["error_message"]
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