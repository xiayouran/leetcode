# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-14 18:35
# Filename: max_sub_array.py
"""
D[i] 表示以X[i]开头的最大子数组之和
Rec[i] 记录数组的结尾索引，开始索引为i
"""
from typing import List
import numpy as np


class Solution:
    def max_sub_array(self, arr: List[int]) -> int:
        """
        递推公式：
        D[i] = X[i] + D[i+1] if D[i+1] > 0 else X[i]
        时间复杂度为O(n)
        """
        n = len(arr)
        D = np.zeros((n, ), dtype=np.int64)
        Rec = np.zeros((n, ), dtype=np.int64)

        D[n - 1] = arr[n - 1]
        Rec[n - 1] = n
        for i in range(n - 2, -1, -1):
            if D[i + 1] > 0:
                D[i] = arr[i] + D[i + 1]
                Rec[i] = Rec[i + 1]
            else:
                D[i] = arr[i]
                Rec[i] = i

        s_max = D[0]
        for i in range(1, n):
            if s_max < D[i]:
                s_max = D[i]

        return s_max


if __name__ == '__main__':
    input_arr = [1, -2, 4, 5, -2, 8, 3, -2, 6, 3, 7, -1]
    solution = Solution()
    output = solution.max_sub_array(input_arr)
    print(output)
