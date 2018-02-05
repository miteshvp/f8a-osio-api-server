import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_liveness():
    """
    Get job service liveness
    

    :rtype: None
    """
    return 'do some magic!'


def get_readiness():
    """
    Get job service readiness
    

    :rtype: None
    """
    return 'do some magic!'
