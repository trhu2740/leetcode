"""
Description of problem
"""

import unittest


# ---------- Solution ----------
class Solution:
    def findLatestTime(self, s: str) -> str:
        return ""


# ---------- Test Cases ----------
class TestCases(unittest.TestCase):
    def test(self):
        sol = Solution()
        with self.subTest():
            assert sol.findLatestTime("??:1?") == "11:19"
        with self.subTest():
            assert sol.findLatestTime("11:5?") == "11:59"
        assertTrue()


def assertTrue():
    print("Test cases passed ✅")


if __name__ == "__main__":
    tests = TestCases()
    tests.test()
