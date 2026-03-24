# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-24 21:52
# Filename: select_sort.py
from typing import List


class Solution:
    def select_sort(self, arr: List[int]) -> List[int]:
        """
        选择排序时间复杂度分析：
        运行次数函数T(n)= n + (n-1) + 3/2n^2 - 1/2n -1 + (n-1) = 3/2n^2 + 5/2n -3
        时间复杂度为O(n^2)
        """
        n = len(arr)
        for i in range(n - 1):          # A[i]与i之后的所有元素逐个比较 n-1次枚举 + 1次比较
            min_idx = i                 # 假设当前位置 i 的元素为最小值 n-1次
            for j in range(i + 1, n):   # 在 i+1 到 n-1 中寻找真正的最小值索引
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]     # 将找到的最小值与当前位置交换 n-1次
            """
            i=0,j=1 n-1+1 + n-1 + n-1
            i=1,j=2 n-2+1 + n-2 + n-2
            i=n-2,j=n-1 1+1 + 1 + 1
            total: (n+2)/2(n-1) + (n-1+1)/2(n-1)2 = 3/2n^2 - 1/2n -1
            """

        return arr


if __name__ == '__main__':
    input_arr = [32, 15, 11, 26, 53, 87, 3, 61]
    solution = Solution()
    output = solution.select_sort(input_arr)
    print(output)
