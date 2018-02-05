import connexion
from swagger_server.models.repo import Repo
from swagger_server.models.report import Report
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_all_repo_report():
    """
    Get healthcheck report for all registered repositories
    

    :rtype: None
    """
    return 'do some magic!'


def get_repo_report(name):
    """
    Get healthcheck report for a registered repository
    
    :param name: github repository name
    :type name: str

    :rtype: Report
    """
    return 'do some magic!'


def scan_repo(repos):
    """
    Scan registered repositories
    
    :param repos: List of registered repositories. Wildcard character &#39;*&#39; is supported for all repositories.
    :type repos: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        repos = [Repo.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'
