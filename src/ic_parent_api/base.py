"""Infinite Campus Base Helpers.

Borrowed from pygrocy (https://github.com/SebRut/pygrocy)
"""
import json


def get_val(obj):
    """Get Value."""
    if hasattr(obj, "as_dict"):
        as_attr = getattr(obj, "as_dict")
        return as_attr()
    return obj


class DataModel():
    """Define DataModel."""
    def tojson(self):
        """Convert to JSON."""
        return json.dumps(self.as_dict())

    def as_dict(self):
        """Convert to dict."""
        return {
            k: get_val(getattr(self, k))
            for k, v in self.__class__.__dict__.items()
            if isinstance(v, property)
        }
