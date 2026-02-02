# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    liyanpeng@people-ai.cn
# Datetime: 2026/2/2 16:59
# Filename: bubble_sort.py
from typing import List


class Solution:
    def bubble_sort(self, arr: List[int]) -> List[int]:
        """
        冒泡排序时间复杂度分析：
        第1轮：执行次数：n-1(只考虑赋值操作)
        第2轮：执行次数：n-2
        ...
        第n-1轮：执行次数：1
        运行次数函数T(n)=(1+n-1)*(n-1)/2=n(n-1)/2
        时间复杂度为O(n^2)
        :param arr: [32,15,11,26,53,87,3,61]
        :return: [3,11,15,26,32,53,61,87]
        """
        n = len(arr)
        for i in range(1, n):   # 外层循环 n-1轮
            is_swapped = False

            for j in range(n-i):    # 内层循环
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_swapped = True

            if not is_swapped:
                break   # 本轮没有发生交换，提前结束

        return arr


if __name__ == '__main__':
    solution = Solution()
    output = solution.bubble_sort([32,15,11,26,53,87,3,61])
    print(output)
