# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-02-02 18:22
# Filename: insert_sort.py
from typing import List


class Solution:
    def insert_sort(self, arr: List[int]) -> List[int]:
        """
        插入排序时间复杂度分析：
        运行次数函数T(n)= n + (n-1)*3 + (3/2n^2 - 1/2n -1) = 3/2n^2 + 7/2n - 4
        时间复杂度为O(n^2)
        """
        n = len(arr)
        for j in range(1, n):   # 从第二个元素开始(第一个元素默认已排序)  n-1次枚举+1次比较=n次
            key = arr[j]        # 当前要插入的元素                      n-1次
            i = j - 1           # 从已排序部分的末尾开始比较             n-1次

            while i >= 0 and arr[i] > key:  # 将比key大的元素向后移动一位
                arr[i + 1] = arr[i]
                i -= 1
            """
            j=1,i=0 1+1+1 + 1次
            j=2,i=1 1+1+1 + 1+1+1 + 1次
            j=n-1,i=n-2 (n-1)(1+1+1) + 1次
            total: (2+n)/2(n-1) + (1+n-1)/2(n-1)2 = 3/2n^2 - 1/2n -1
            """

            arr[i + 1] = key  # 将key插入到正确位置                       n-1次

        return arr


if __name__ == '__main__':
    input_arr = [32, 15, 11, 26, 53, 87, 3, 61]
    solution = Solution()
    output = solution.insert_sort(input_arr)
    print(output)
