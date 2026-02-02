# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    liyanpeng@people-ai.cn
# Datetime: 2026/2/2 18:02
# Filename: select_sort.py
from typing import List


class Solution:
    def select_sort(self, arr: List[int]) -> List[int]:
        """
        选择排序时间复杂度分析：
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
        for i in range(n-1):    # 外层循环：n-1轮
            min_idx = i     # 先假设当前位置为最小值，即每轮乱序的第一个位置

            for j in range(i+1, n):     # 内层循环：在i+1到n-1范围内寻找真正的最小值
                if arr[j] < arr[min_idx]:
                    min_idx = j  # 更新最小值位置

            if min_idx != i:    # 将找到的最小值与当前位置交换
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr


if __name__ == '__main__':
    solution = Solution()
    output = solution.select_sort([32,15,11,26,53,87,3,61])
    print(output)
