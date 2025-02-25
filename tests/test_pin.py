import unittest
from pin_actions.pin import get_pinned_sha

class TestPinActions(unittest.TestCase):
    def test_get_pinned_sha(self):
        sha = get_pinned_sha("actions/setup-python", "v5")
        self.assertTrue(len(sha) == 40)

if __name__ == '__main__':
    unittest.main()
