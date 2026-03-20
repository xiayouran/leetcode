# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-20 23:13
# Filename: weighted_activity_selection.py
"""
p[i]在a_i开始前最后结束的活动
D[i]在集合{a_i,a_2,..,a_i}中找到的不冲突活动的最大权重和
Rec[i]记录是否选择活动a_i
"""
from typing import List, Tuple
import bisect


class Activity:
    def __init__(self, name: str, start: int, end: int, weight: int):
        self.name = name    # 活动的名称
        self.start = start  # 活动的开始时间
        self.end = end      # 活动的结束时间
        self.weight = weight    # 活动的收益

    # 定义小于比较（按活动结束时间）
    def __lt__(self, other):
        return self.end < other.end


class Solution:
    def weighted_activity_selection(self, F: List[Activity]):
        """
        递推公式：D[i] = max(D[p[i]] + w_i, D[i-1])
        时间复杂度为O(nlogn)
        """
        # 按结束时间升序排序
        sorted_acts = sorted(F, key=lambda x: x.end)

        n = len(sorted_acts)
        # 结束时间列表，用于二分查找
        ends = [act.end for act in sorted_acts]

        p = [0] * n
        for i in range(n):
            # 分查找最后一个结束时间 <= act.start 的活动
            j = bisect.bisect_right(ends, sorted_acts[i].start, 0, i)
            p[i] = j - 1

        D = [0] * (n + 1)
        Rec = [False] * n
        for j in range(0, n):
            if D[p[j]] + sorted_acts[j].weight > D[j - 1]:  # 选择活动a_j
                D[j] = D[p[j]] + sorted_acts[j].weight
                Rec[j] = True
            else:
                D[j] = D[j - 1]
                Rec[j] = False

        k = n - 1
        while k >= 0:
            if Rec[k]:
                print(sorted_acts[k].name)
                k = p[k]
            else:
                k -= 1


if __name__ == '__main__':
    F = [
        Activity("a1", 1, 4, weight=1),
        Activity("a2", 3, 5, weight=6),
        Activity("a3", 0, 6, weight=4),
        Activity("a4", 4, 7, weight=7),
        Activity("a5", 3, 9, weight=3),
        Activity("a6", 5, 9, weight=12),
        Activity("a7", 6, 10, weight=2),
        Activity("a8", 8, 11, weight=9),
        Activity("a9", 8, 12, weight=11),
        Activity("a10", 2, 14, weight=8),
    ]
    solution = Solution()
    solution.weighted_activity_selection(F)
