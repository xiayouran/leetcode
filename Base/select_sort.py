# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-02-02 18:02
# Filename: select_sort.py
from typing import List


class Solution:
    def select_sort(self, arr: List[int]) -> List[int]:
        """
        选择排序时间复杂度分析：
        运行次数函数T(n)= n + 3/2n^2 - 1/2n -1 = 3/2n^2 + 1/2n -1
        时间复杂度为O(n^2)
        """
        n = len(arr)
        for i in range(n - 1):            # A[i]与i之后的所有元素逐个比较 n-1次枚举 + 1次比较
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
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
