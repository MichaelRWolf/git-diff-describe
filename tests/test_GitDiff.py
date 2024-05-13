from unittest import TestCase

from approvaltests import verify

from GitDiff import GitDiff


class TestGitDiff(TestCase):
    def test_describe_empty_object(self):
        obj = GitDiff()
        result = obj.asTextDescription()
        verify(result)
