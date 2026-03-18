# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-18 21:18
# Filename: minimum_edit_distance.py
"""
D[i,j]  字符串s[1..i]变为t[1..j]的最小编辑距离
Rec[i,j]    记录子问题的来源
U 上 D[i-1,j]  删除s[i]
L 左 D[i,j-1]  插入t[j]
LU 左上 D[i-1,j-1]    替换或无操作(s[i]替换为t[j])
优先选择替换(LU)
"""
from typing import List
import numpy as np


class Solution:
    def minimum_edit_distance(self, s: str, t: str) -> None:
        """
        递推公式：
        删除：D[i,j] = D[i-1,j] + 1
        插入：D[i,j] = D[i,j-1] +
        替换：D[i,j] = D[i-1,j-1] + 0 if s[i] == t[j] else D[i-1,j-1] + 1
        时间复杂度为O(n·m)
        """
        n, m = len(s), len(t)
        D = np.zeros((n + 1, m + 1), dtype=np.int64)
        Rec = np.zeros((n + 1, m + 1), dtype=np.int64)
        for i in range(n + 1):
            D[i, 0] = i
            Rec[i, 0] = 1   # U
        for j in range(m + 1):
            D[0, j] = j
            Rec[0, j] = 2   # L

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                c = 0
                if s[i - 1] != t[j - 1]:
                    c = 1
                delete = D[i - 1, j] + 1
                insert = D[i, j - 1] + 1
                replace = D[i - 1, j - 1] + c

                if min(delete, insert, replace) == replace:     # 替换优先
                    D[i, j] = D[i - 1, j - 1] + c
                    Rec[i, j] = 3  # LU
                elif min(delete, insert, replace) == insert:
                    D[i, j] = D[i, j - 1] + 1
                    Rec[i, j] = 2   # L
                else:
                    D[i, j] = D[i - 1, j] + 1
                    Rec[i, j] = 1  # U

        self.print_MED(Rec, s, t, n, m)

    def print_MED(self, Rec: np.ndarray, s: str, t: str, i: int, j: int) -> None:
        if i == 0 and j == 0:
            return

        if Rec[i, j] == 1:
            self.print_MED(Rec, s, t, i - 1, j)
            print(f'删除{s[i - 1]}')
        elif Rec[i, j] == 2:
            self.print_MED(Rec, s, t, i, j - 1)
            print(f'插入{t[j - 1]}')
        else:
            self.print_MED(Rec, s, t, i - 1, j - 1)
            if s[i - 1] == t[j - 1]:
                print('SKIP')
            else:
                print(f'{s[i - 1]}替换为{t[j - 1]}')


if __name__ == '__main__':
    s = 'ABCBDAB'
    t = 'BDCABA'
    solution = Solution()
    solution.minimum_edit_distance(s, t)
