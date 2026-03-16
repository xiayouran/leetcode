# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-16 22:01
# Filename: selection.py
from typing import List
import random


class Solution:
    def selection(self, arr: List[int], left: int, right: int, k: int) -> int:
        """
        时间复杂度分析：
        运行次数函数T(n)= O(n) + ?
        时间复杂度为O(n)  数学期望
        """
        q = self.partition(arr, left, right)    # O(n)
        if k == (q - left + 1):
            return arr[q]
        elif k < (q - left + 1):
            return self.selection(arr, left, q - 1, k)
        else:
            return self.selection(arr, q + 1, right, k - (q - left + 1))

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
    input_arr = [21, 17, 37, 28, 13, 14, 22, 52, 40, 24, 48, 4, 47, 8, 42, 18]
    solution = Solution()
    output = solution.selection(input_arr, left=0, right=len(input_arr) - 1, k=8)
    print(output)
