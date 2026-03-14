# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-14 18:35
# Filename: max_sub_array.py
from typing import List
import math


class Solution:
    def max_sub_array(self, arr: List[int], left: int, right: int) -> int:
        """
        时间复杂度分析：
        运行次数函数T(n)= 2T(n/2) + O(n)
        时间复杂度为O(nlogn)
        """
        if left == right:  # 只有一个元素，直接返回
            return arr[left]

        mid = (left + right) // 2
        s1_max = self.max_sub_array(arr, left, mid)      # T(n/2)
        s2_max = self.max_sub_array(arr, mid + 1, right)   # T(n/2)
        s3_max = self.crossing_sub_array(arr, left, mid, right)     # O(n)
        s_max = max(s1_max, s2_max, s3_max)

        return s_max

    def crossing_sub_array(self, arr: List[int], left: int, mid: int, right: int) -> int:
        """
        子数组S3有可能横跨S1和S2两个数组
        S3可分为左右两部分：
        S3-left：以A[mid]为结尾的最大子数组之和
        S3-right：以A[mid+1]为开头的最大子数组之和
        S3 = S3-left + S3-right

        S3-left求解：从A[mid]向前遍历求和，并记录最大值
        S3-right求解：从A[mid+1]向后遍历求和，并记录最大值
        """
        left_max = -math.inf
        left_sum = 0
        for l in range(mid, left - 1, -1):
            left_sum += arr[l]
            left_max = max(left_max, left_sum)

        right_max = -math.inf
        right_sum = 0
        for r in range(mid + 1, right + 1):
            right_sum += arr[r]
            right_max = max(right_max, right_sum)

        s3_max = left_max + right_max
        return s3_max


if __name__ == '__main__':
    input_arr = [1, -2, 4, 5, -2, 8, 3, -2, 6, 3, 7, -1]
    solution = Solution()
    output = solution.max_sub_array(input_arr, left=0, right=len(input_arr) - 1)
    print(output)
