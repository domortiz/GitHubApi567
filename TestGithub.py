import unittest
from GetRepoInfo import check_repo


class TestRepoInfo(unittest.TestCase):
    def test_np_name(self):
        self.assertEqual(check_repo(''), False)

    def test_name(self):
        self.assertEqual(check_repo('richkempinski'), True)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
