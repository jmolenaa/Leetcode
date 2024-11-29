from typing import List


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		index = 0
		for i, num in enumerate(nums[:-2]):
			if nums[i] != nums[i + 1] or nums[i] != nums[i + 2]:
				nums[index] = nums[i]
				index += 1
		for num in nums[-2:]:
			nums[index] = num
			index += 1
		return index

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
	test([2, 2, 3], [2, 2, 3])
	test([0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4], [0, 0, 1, 1, 2, 2, 3, 3, 4])
	test([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3])
	test([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3])
	test([1], [1])
