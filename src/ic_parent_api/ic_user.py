"""Infinite Campus User data need to authenticate"""

from dataclasses import dataclass


@dataclass
class InfiniteCampusUser:
    """Infinite Campus User data need to authenticate"""
    username: str
    password: str
    district: str
