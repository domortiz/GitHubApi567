import unittest
from unittest import mock
from GetRepoInfo import check_repo


class TestRepoInfo(unittest.TestCase):
    def test_no_name(self):
        with mock.patch('GetRepoInfo.check_repo', create=False) as MockCheckRepo:
            MockCheckRepo.return_value = False
            self.assertEqual(MockCheckRepo(''), False)

    def test_name(self):
        with mock.patch('GetRepoInfo.check_repo', create=False) as MockCheckRepo:
            MockCheckRepo.return_value = True
            self.assertEqual(MockCheckRepo('domortiz'), True)


if __name__ == '__main__':
    unittest.main()
