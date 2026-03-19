# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-19 22:40
# Filename: fractional_knapsack.py
from typing import List


class Solution:
    def fractional_knapsack(self, n: int, p: List[int], v: List[int], C: int) -> List[tuple[int, int]]:
        """
        时间复杂度为O(nlogn)
        """
        # 商品数量n，各商品的价值p，各商品的体积v，背包容量C
        # 先对商品按性价比进行排序 O(nlogn)
        ratio = sorted([(i, p[i] / v[i]) for i in range(n)], key=lambda x: x[1], reverse=True)

        product_list = []
        i, ans = 1, 0
        while C > 0 and i <= n:     # 背包未满且商品还有剩余
            real_index = ratio[i - 1][0]
            if v[real_index] <= C:
                product_list.append((real_index, 1))   # 选择商品i
                ans += p[real_index]
                C -= v[real_index]
            else:
                product_list.append((real_index, C))    # 选择C体积的商品i
                ans += p[real_index] * C / v[real_index]
                C = 0
            i += 1

        print(ans)
        return product_list


if __name__ == '__main__':
    super_market = [
        # 商品，价格，体积
        ['橙汁', 36, 200],
        ['苹果汁', 16, 100],
        ['西瓜汁', 45, 300],
        ['苏打水', 60, 600],
        ['汽水', 10, 250],
    ]
    solution = Solution()
    output = solution.fractional_knapsack(
        n=len(super_market),
        p=[product[1] for product in super_market],
        v=[product[2] for product in super_market],
        C=800
    )
    for index, v in output:
        if v == 1:
            print(f'选择商品 {super_market[index][0]} {super_market[index][2]} ml')
        else:
            print(f'选择商品 {super_market[index][0]} {v} ml')
