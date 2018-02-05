import connexion
from swagger_server.models.repo import Repo
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def deregister_repo(repo):
    """
    Deregister a monitored repository
    
    :param repo: A registered repository
    :type repo: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        repo = Repo.from_dict(connexion.request.get_json())
    return 'do some magic!'


def register_repo(repo):
    """
    Register a repository for monitoring
    
    :param repo: A registered repository
    :type repo: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        repo = Repo.from_dict(connexion.request.get_json())
    return 'do some magic!'


def revive_repo(repo):
    """
    Revive a suspended repository for monitoring
    
    :param repo: A registered repository
    :type repo: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        repo = Repo.from_dict(connexion.request.get_json())
    return 'do some magic!'


def suspend_repo(repo):
    """
    Suspend a monitored repository temporarily
    
    :param repo: A registered repository
    :type repo: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        repo = Repo.from_dict(connexion.request.get_json())
    return 'do some magic!'
