# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.repo import Repo
from swagger_server.models.report import Report
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestHealthcheckServicesController(BaseTestCase):
    """ HealthcheckServicesController integration test stubs """

    def test_get_all_repo_report(self):
        """
        Test case for get_all_repo_report

        Get healthcheck report for all registered repositories
        """
        response = self.client.open('/api/v1//reports',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_repo_report(self):
        """
        Test case for get_repo_report

        Get healthcheck report for a registered repository
        """
        response = self.client.open('/api/v1//reports/{name}'.format(name='name_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_scan_repo(self):
        """
        Test case for scan_repo

        Scan registered repositories
        """
        repos = [Repo()]
        response = self.client.open('/api/v1//scan',
                                    method='POST',
                                    data=json.dumps(repos),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
