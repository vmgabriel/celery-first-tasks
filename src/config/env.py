"""
Module of Environments
"""

import os
from dotenv import load_dotenv

load_dotenv()


configuration = {
    # Confiration of Broker
    'user_broker': os.getenv('USER_BROCKER'),
    'pass_broker': os.getenv('PASWORD_BROKER'),

    'url_broker': os.getenv('PASSWORD_BROKER') \
    if os.getenv('PASSWORD_BROKER') \
    else 'localhost',

    'protocol_broker': 'amqp',
    'port_broker': 6379,
}
