# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-14 18:03
# Filename: binary_search.py
from typing import List


class Solution:
    def binary_search(self, arr: List[int], left: int, right: int, x: int) -> int:
        """
        二分搜索时间复杂度分析：
        运行次数函数T(n)= T(n/2) + O(1)
        时间复杂度为O(logn)
        """
        if left > right:    # 递归终止条件1
            return -1

        mid = (left + right) // 2
        if arr[mid] == x:   # 递归终止条件2
            return mid
        if x < arr[mid]:
            return self.binary_search(arr, left, mid - 1, x)  # 不再考虑mid，所以是mid-1
        else:
            return self.binary_search(arr, mid + 1, right, x)


if __name__ == '__main__':
    input_arr = [3, 11, 15, 26, 53, 61, 87]
    solution = Solution()
    output = solution.binary_search(input_arr, left=0, right=len(input_arr) - 1, x=15)
    print(output)
