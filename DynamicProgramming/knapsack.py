# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-16 22:52
# Filename: knapsack.py
"""
P[i,c] 表示在前i个物品中选择，背包容量为c时的最优解（物品总价值最大）
Rec[i,c] 表示在背包容量为c时，第i个物品是否选择
"""
from typing import List
import numpy as np


class Solution:
    def knapsack(self, n: int, p: List[int], v: List[int], C: int) -> List[int]:
        """
        递推公式：P[i,c] = max(P[i-1, c], p_i + P[i-1, c-v_i])
        时间复杂度为O(n·C)
        """
        # 商品数量n，各商品的价值p，各商品的体积v，背包容量C
        # P shanpe:(n + 1, C + 1)
        P = np.zeros((n + 1, C + 1), dtype=np.int64)
        Rec = np.zeros((n + 1, C + 1), dtype=np.int64)

        for i in range(1, n + 1):
            for c in range(1, C + 1):
                # 注意：p[i-1] 和 v[i-1] 才是第i个商品的价值和体积
                if v[i - 1] <= c and p[i - 1] + P[i - 1, c - v[i - 1]] > P[i - 1, c]:
                    # 商品i的体积小于背包容量，且选择商品i引起的背包总价值 > 不选择商品i引起的背包总价值
                    P[i, c] = p[i - 1] + P[i - 1, c - v[i - 1]]
                    Rec[i, c] = 1
                else:
                    P[i, c] = P[i - 1, c]
                    Rec[i, c] = 0

        product_list = []
        K = C
        for i in range(n, 0, -1):
            if Rec[i, K] == 1:
                product_list.append(i)
                K -= v[i - 1]

        return product_list


if __name__ == '__main__':
    super_market = [
        # 商品，价格，体积
        ['啤酒', 24, 10],
        ['汽水', 2, 3],
        ['饼干', 9, 4],
        ['面包', 10, 5],
        ['牛奶', 9, 4],
    ]
    solution = Solution()
    output = solution.knapsack(
        n=len(super_market),
        p=[product[1] for product in super_market],
        v=[product[2] for product in super_market],
        C=13
    )
    for index in output:
        print(f'选择商品 {super_market[index - 1][0]}')
