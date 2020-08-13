
"""
Module of Celery
"""
# Libraries
from typing import Any
from celery import Celery

# Configuration of Celery
from src.config.celery import configuration as conf


app = Celery(
    'queue_1',
    broker='amqp://localhost:6379//'
)


@app.task
def add(_x: Any, _y: Any) -> Any:
    """Add data"""
    return _x + _y


@app.task
def mult(_x: Any, _y: Any) -> Any:
    """Add data"""
    return _x * _y
