# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-17 22:56
# Filename: longest_common_subsequence.py
"""
C[i,j] 表示X[1..i]和Y[1..j]的最长公共子序列长度
Rec[i,j] 记录子问题的来源
LU 表示 C[i,j] = C[i-1,j-1] + 1
U  表示 C[i,j] = C[i-1,j]
L  表示 C[i,j] = C[i,j-1]
"""
from typing import List
import numpy as np


class Solution:
    def longest_common_subsequence(self, X: str, Y: str) -> None:
        """
        递推公式：C[i,j] = C[i-1,j-1]+1 if x_i == x_j else max(C[i-1,j],C[i,j-1])
        时间复杂度为O(n·m)
        """
        n, m = len(X), len(Y)
        # C = [[0 for _ in range(m)] for _ in range(n)]
        C = np.zeros((n + 1, m + 1), dtype=np.int64)
        Rec = np.zeros((n + 1, m + 1), dtype=np.int64)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if X[i - 1] == Y[j - 1]:
                    C[i, j] = C[i - 1, j - 1] + 1
                    Rec[i, j] = 3   # LU
                elif C[i - 1, j] >= C[i, j - 1]:
                    C[i, j] = C[i - 1, j]
                    Rec[i, j] = 2   # U
                else:
                    C[i, j] = C[i, j - 1]
                    Rec[i, j] = 1   # L

        print(C[n, m])
        self.print_LCS(Rec, X, n, m)

    def print_LCS(self, rec: np.ndarray, X: str, i: int, j: int) -> None:
        if i == 0 or j == 0:
            return

        if rec[i, j] == 3:
            self.print_LCS(rec, X, i - 1, j - 1)
            print(X[i - 1], end='')
        elif rec[i, j] == 2:
            self.print_LCS(rec, X, i - 1, j)
        else:
            self.print_LCS(rec, X, i, j - 1)


if __name__ == '__main__':
    X = 'ABCBDAB'
    Y = 'BDCABA'
    solution = Solution()
    solution.longest_common_subsequence(X, Y)
