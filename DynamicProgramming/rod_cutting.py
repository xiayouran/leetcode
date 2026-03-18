# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-18 22:29
# Filename: rod_cutting.py
"""
C[j]  切割长度为j的钢条可获得的最大总收益
p[i]  钢条长度为i的价格
Rec[j]记录长度为j钢条的最优切割方案
不切：Rec[j] = j
切割：Rec[j] = k
"""
from typing import List


class Solution:
    def rod_cutting(self, p: List[int], n: int) -> None:
        """
        递推公式：
        C[j] = max(p[i] + C[j-i], p[j]) 1<=i<=j-1
        时间复杂度为O(n^2)
        """
        C = [0] * (n + 1)
        Rec = [0] * (n + 1)
        for j in range(1, n + 1):   # 钢条长度，从1长到n
            q = p[j - 1]
            Rec[j] = j      # 不切钢条
            for i in range(1, j):   # 枚举切割区间，从i=1处切割，直到j-1
                if q < p[i - 1] + C[j - i]:
                    q = p[i - 1] + C[j - i]
                    Rec[j] = i  # 从i处切割
            C[j] = q

        # 输出最优方案
        while n > 0:
            print(Rec[n])
            n -= Rec[n]


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 24]
    solution = Solution()
    solution.rod_cutting(p, n=10)
