from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                nums1.pop(-1)
                i += 1
                m += 1
                j += 1

        while j < n:
            nums1.insert(i, nums2[j])
            nums1.pop(-1)
            j += 1
            i += 1


def test(nums1, nums2):
    n = len(nums2)
    m = len(nums1)
    nums1 = nums1 + n * [0]
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)


if __name__ == '__main__':
    test([1, 2, 3], [2, 5, 6])
    test([1], [])
    test([0], [1])
    test([1, 2, 3, 100, 299, 10001, 20223], [2, 5, 6, 8, 10, 13, 16, 17])

