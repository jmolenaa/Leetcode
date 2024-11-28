from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        index = 0
        numslen = len(nums)
        while i < numslen - 1:
            if nums[i] != nums[i + 1]:
                nums[index] = nums[i]
                index += 1
            i += 1

        nums[index] = nums[i]

        return index + int(numslen != 0)


def test(nums, expected):
    expected.sort()

    solution = Solution()
    k = solution.removeDuplicates(nums)

    assert k == len(expected)
    newList = nums[:k]
    newList.sort()

    for i in range(0, k):
        assert newList[i] == expected[i]


if __name__ == '__main__':
    test([1, 2, 3], [1, 2, 3])
    test([2, 2, 3], [2, 3])
    test([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])
