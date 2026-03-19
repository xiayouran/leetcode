# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-19 21:22
# Filename: matrix_chain_multiplication.py
"""
D[i,j]  计算矩阵链U_{i..j}所需标量乘法的最小次数 (p_{i-1},p_i)x...x(p_{j-1},p_j) U_i shape:(p_{i-1}, p_i)
Rec[i,j]记录矩阵链U_{i..j}的最优分割位置
"""
from typing import List
import numpy as np


class Solution:
    def matrix_chain_multiplication(self, p: List[int], n: int) -> None:
        """
        递推公式：
        D[i,j] = D[i,k] + D[k+1,j] + p_{i-1}p_kp_j
        时间复杂度为O(n^3)
        """
        D = np.full((n, n), np.inf, dtype=np.float64)
        for i in range(1, n):
            D[i, i] = 0
        Rec = np.zeros((n, n), dtype=np.int64)

        for l in range(2, n + 1):   # 从长度为2的链开始计算，直到计算n个矩阵链相乘
            for i in range(0, n - l + 1):   # 链的起始矩阵索引
                j = i + l - 1               # 链的结束矩阵索引
                for k in range(i, j):       # 枚举所有分割位置
                    q = D[i, k] + D[k + 1, j] + p[i] * p[k + 1] * p[j + 1]
                    if q < D[i, j]:
                        D[i, j] = q
                        Rec[i, j] = k
        
        self.print_matrix_chain(Rec, 0, 5)

    def print_matrix_chain(self, Rec, i, j) -> None:
        if i == j:
            print(f'U_{i + 1}', end='')
            return

        print('(', end='')
        self.print_matrix_chain(Rec, i, Rec[i, j])
        print(')(', end='')
        self.print_matrix_chain(Rec, Rec[i, j] + 1, j)
        print(')', end='')


if __name__ == '__main__':
    p = [2, 3, 7, 9, 5, 2, 4]
    solution = Solution()
    solution.matrix_chain_multiplication(p, n=6)
