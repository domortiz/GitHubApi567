import unittest
from GetRepoInfo import check_repo


class TestRepoInfo(unittest.TestCase):
    def test_no_name(self):
        self.assertEqual(check_repo(''), False)

    def test_name(self):
        self.assertEqual(check_repo('domortiz'), True)


if __name__ == '__main__':
    unittest.main()
