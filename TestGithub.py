import unittest
from GetRepoInfo import check_repo


class TestRepoInfo(unittest.TestCase):
    def test_np_name(self):
        self.assertEqual(check_repo(''), 'No username entered')


if __name__ == '__main__':
    unittest.main()
