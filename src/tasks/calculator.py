"""
Module of Calculator
"""

# Libraries
from typing import Any

# task
from celery import app as queue

@queue.task
def add(_x: Any, _y: Any) -> Any:
    """Add data"""
    return _x + _y
