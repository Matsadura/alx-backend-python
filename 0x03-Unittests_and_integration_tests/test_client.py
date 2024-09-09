#!/usr/bin/env python3
"""Module for testing client"""


from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """Class for Testing Github Org Client"""

    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test GithubOrgClient.org and see if it returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(
                f'https://api.github.com/orgs/{input}')

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that the result of _public_repos_url is the expected
        one based on the mocked payload
        """
        mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test-org/repos"
                }
        client = GithubOrgClient("test-org")
        result = client._public_repos_url
        expected = "https://api.github.com/orgs/test-org/repos"

        self.assertEqual(result, expected)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, expected):
        """unit-test for GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
        )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class for Integration test of fixtures"""

    @classmethod
    def setUpClass(cls):
        config = {'return_value.json.side_effect': [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                    ]}
        cls.get_patcher = patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    @classmethod
    def teardownClass(cls):
        """class method to stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method"""
        client = GithubOrgClient("google")

        self.assertEqual(
                client.public_repos(license="apache-2.0"), self.apache2_repos)
