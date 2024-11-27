from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        removedElements = 0
        i = 0
        numsLen = len(nums)
        while i < numsLen - removedElements:

            if nums[i] == val:
                nums[i] ^= nums[numsLen - removedElements - 1]
                nums[numsLen - removedElements - 1] ^= nums[i]
                nums[i] ^= nums[numsLen - removedElements - 1]
                removedElements += 1
                continue
            i += 1
        return numsLen - removedElements


def test(nums, expected, value):
    expected.sort()

    solution = Solution()
    k = solution.removeElement(nums, value)
    assert k == len(expected)

    newList = nums[:k]
    newList.sort()

    for i in range(0, k):
        assert newList[i] == expected[i]



if __name__ == '__main__':
    test([1, 2, 3], [1, 3], 2)
    test([3, 2, 2, 3], [2, 2], 3)
    test([0, 1, 2, 2, 3, 0, 4, 2], [0, 1, 3 ,0, 4], 2)

