"""
3114. Latest Time You Can Obtain After Replacing Characters

You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".

12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.

You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible.

Return the resulting string.
"""

import unittest


class Solution:
    def findLatestTime(self, s: str) -> str:
        # First check if the string doesn't contain any question marks
        if "?" not in s:
            return s
        sList = list(s)
        # Next, replace question marks in the string with the highest value possible
        for index, char in enumerate(s):
            if char == "?":
                if index == 0:
                    if sList[1] == "0" or sList[1] == "1" or sList[1] == "?":
                        sList[index] = "1"
                    else:
                        sList[index] = "0"
                elif index == 1:
                    if sList[0] == "0":
                        sList[index] = "9"
                    else:
                        sList[index] = "1"
                elif index == 3:
                    sList[index] = "5"
                elif index == 4:
                    sList[index] = "9"
        return "".join(sList)


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
