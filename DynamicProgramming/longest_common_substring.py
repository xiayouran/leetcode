# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-18 21:01
# Filename: longest_common_substring.py
"""
C[i,j]  表示在X[1..i]和Y[1..j]中，以x_i和y_j结尾的最长公共子串长度
p_max   为最长公共子串末尾的位置
l_max   为最长公共子串长度
"""
from typing import List
import numpy as np


class Solution:
    def longest_common_substring(self, X: str, Y: str) -> None:
        """
        递推公式：C[i,j] = C[i-1,j-1]+1 if x_i == x_j else 0
        时间复杂度为O(n·m)
        """
        n, m = len(X), len(Y)
        p_max, l_max = 0, 0
        # C = [[0 for _ in range(m)] for _ in range(n)]
        C = np.zeros((n + 1, m + 1), dtype=np.int64)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if X[i - 1] == Y[j - 1]:
                    C[i, j] = C[i - 1, j - 1] + 1
                    if C[i, j] > l_max:
                        l_max = C[i, j]
                        p_max = i

        self.print_LCS(X, p_max, l_max)

    def print_LCS(self, X: str, p_max: int, l_max: int) -> None:
        if l_max == 0:
            return
        print(X[p_max - l_max: p_max])


if __name__ == '__main__':
    X = 'DBDAB'
    Y = 'CABB'
    solution = Solution()
    solution.longest_common_substring(X, Y)
