# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-20 22:57
# Filename: activity_selection.py
from typing import List, Tuple


class Activity:
    def __init__(self, name: str, start: int, end: int):
        self.name = name    # 活动的名称
        self.start = start  # 活动的开始时间
        self.end = end      # 活动的结束时间

    # 定义小于比较（按活动结束时间）
    def __lt__(self, other):
        return self.end < other.end


class Solution:
    def activity_selection(self, F: List[Activity]):
        """
        时间复杂度为O(nlogn)
        """
        F = sorted(F, key=lambda x: x.end, reverse=False)
        select_list = []
        select_list.append(F[0])
        k = 0
        for i in range(1, len(F)):
            if F[i].start >= F[k].end:
                select_list.append(F[i])
                k = i
        return select_list


if __name__ == '__main__':
    F = [
        Activity("a1", 1, 4),
        Activity("a2", 3, 5),
        Activity("a3", 0, 6),
        Activity("a4", 4, 7),
        Activity("a5", 3, 9),
        Activity("a6", 5, 9),
        Activity("a7", 6, 10),
        Activity("a8", 8, 11),
        Activity("a9", 8, 12),
        Activity("a10", 2, 14),
        Activity("a11", 12, 16),
    ]
    solution = Solution()
    select_list = solution.activity_selection(F)
    for activity in select_list:
        print(activity.name)
