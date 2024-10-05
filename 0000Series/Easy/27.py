"""
27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

import unittest


# ---------- Solution ----------
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        for _ in range(nums.count(val)):
            nums.remove(val)
        print(nums)
        return len(nums)


# ---------- Test Cases ----------
class TestCases(unittest.TestCase):
    def test(self):
        sol = Solution()
        with self.subTest():
            assert sol.removeElement(nums=[3, 2, 2, 3], val=3) == 2
        with self.subTest():
            assert sol.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2) == 5
        assertTrue()


def assertTrue():
    print("Test cases passed ✅")


if __name__ == "__main__":
    tests = TestCases()
    tests.test()
