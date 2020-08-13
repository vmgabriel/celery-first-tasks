
"""
Module of Celery
"""
# Libraries
from celery import Celery

# Configuration of Celery
from src.config.celery import configuration as conf


print('configuration - ', conf)

app = Celery(
    conf.get('virtual_host'),
    broker=conf.get('broker'),
    include=['src.tasks.calculator']
)
