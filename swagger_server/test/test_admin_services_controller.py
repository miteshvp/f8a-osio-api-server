# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.repo import Repo
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAdminServicesController(BaseTestCase):
    """ AdminServicesController integration test stubs """

    def test_deregister_repo(self):
        """
        Test case for deregister_repo

        Deregister a monitored repository
        """
        repo = Repo()
        response = self.client.open('/api/v1//repos/deregister',
                                    method='POST',
                                    data=json.dumps(repo),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_register_repo(self):
        """
        Test case for register_repo

        Register a repository for monitoring
        """
        repo = Repo()
        response = self.client.open('/api/v1//repos/register',
                                    method='POST',
                                    data=json.dumps(repo),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_revive_repo(self):
        """
        Test case for revive_repo

        Revive a suspended repository for monitoring
        """
        repo = Repo()
        response = self.client.open('/api/v1//repos/revive',
                                    method='POST',
                                    data=json.dumps(repo),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_suspend_repo(self):
        """
        Test case for suspend_repo

        Suspend a monitored repository temporarily
        """
        repo = Repo()
        response = self.client.open('/api/v1//repos/suspend',
                                    method='POST',
                                    data=json.dumps(repo),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
