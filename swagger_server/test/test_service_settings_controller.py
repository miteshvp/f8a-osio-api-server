# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestServiceSettingsController(BaseTestCase):
    """ ServiceSettingsController integration test stubs """

    def test_get_liveness(self):
        """
        Test case for get_liveness

        Get job service liveness
        """
        response = self.client.open('/api/v1//liveness',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_readiness(self):
        """
        Test case for get_readiness

        Get job service readiness
        """
        response = self.client.open('/api/v1//readiness',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
