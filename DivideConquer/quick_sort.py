# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-14 22:24
# Filename: quick_sort.py
from typing import List
import random


class Solution:
    def quick_sort(self, arr: List[int], left: int, right: int) -> None:
        """
        归并排序时间复杂度分析：
        运行次数函数T(n)= O(n) + ?
        时间复杂度为O(nlogn)
        """
        if left < right:
            q = self.partition(arr, left, right)    # O(n)
            self.quick_sort(arr, left, q - 1)
            self.quick_sort(arr, q + 1, right)

    def partition(self, arr: List[int], left: int, right: int) -> int:
        # x = arr[right]  # 选取最后一个主元

        index = random.randint(left, right)     # 随机选取主元位置
        arr[index], arr[right] = arr[right], arr[index]     # 将主元放到最后
        x = arr[right]

        i = left - 1
        for j in range(left, right):
            if arr[j] <= x:
                arr[i + 1], arr[j] = arr[j], arr[i + 1]     # 交换，小的放前
                i += 1
        arr[i + 1], arr[right] = arr[right], arr[i + 1]     # 交换主元
        q = i + 1   # 主元位置

        return q


if __name__ == '__main__':
    input_arr = [32, 15, 11, 26, 53, 87, 3, 61]
    solution = Solution()
    solution.quick_sort(input_arr, left=0, right=len(input_arr) - 1)
    print(input_arr)
