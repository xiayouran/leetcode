# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    liyanpeng@people-ai.cn
# Datetime: 2026/2/2 18:22
# Filename: insert_sort.py
from typing import List


class Solution:
    def insert_sort(self, arr: List[int]) -> List[int]:
        """
        插入排序时间复杂度分析：
        第1轮：执行次数：1(只考虑赋值操作)
        第2轮：执行次数：2
        ...
        第n-1轮：执行次数：n-1
        运行次数函数T(n)=(1+n-1)*(n-1)/2=n(n-1)/2
        时间复杂度为O(n^2)
        :param arr: [32,15,11,26,53,87,3,61]
        :return: [3,11,15,26,32,53,61,87]
        """
        n = len(arr)
        for i in range(1, n):   # 从第二个元素开始(第一个元素默认已排序)
            key = arr[i]    # 当前要插入的元素
            j = i - 1   # 从已排序部分的末尾开始比较

            while j >= 0 and arr[j] > key:  # 将比key大的元素向后移动
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = key  # 将key插入到正确位置

        return arr


if __name__ == '__main__':
    solution = Solution()
    output = solution.insert_sort([32,15,11,26,53,87,3,61])
    print(output)
