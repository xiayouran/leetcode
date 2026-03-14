# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-14 21:57
# Filename: inversion_counting.py
from typing import List
import copy


class Solution:
    def inversion_counting(self, arr: List[int], left: int, right: int) -> int:
        """
        归并排序时间复杂度分析：
        运行次数函数T(n)= 2T(n/2) + O(n)
        时间复杂度为O(nlogn)
        """
        if left >= right:  # 只有一个元素，直接返回
            return 0

        mid = (left + right) // 2
        s1_count = self.inversion_counting(arr, left, mid)         # T(n/2)
        s2_count = self.inversion_counting(arr, mid + 1, right)    # T(n/2)
        s3_count = self.merge_count(arr, left, mid, right)       # O(n)
        count = s1_count + s2_count + s3_count

        return count

    def merge_count(self, arr: List[int], left: int, mid: int, right: int) -> int:
        arr_tmp = copy.deepcopy(arr)
        i, j, k = left, mid + 1, 0      # k为最终输出有序数组的索引
        s3_count = 0
        while i <= mid and j <= right:
            if arr_tmp[i] <= arr_tmp[j]:
                arr[left + k] = arr_tmp[i]    # 小的放前面
                i += 1
            else:
                arr[left + k] = arr_tmp[j]    # i<j & A[i]>A[j] 是逆序对
                j += 1
                s3_count += (mid - i + 1)
            k += 1

        # 处理剩余部分
        # 两块排好序的子数组，一块已经全部放入，另一块的剩余部分直接放入
        if i <= mid:
            arr[left + k:right + 1] = arr_tmp[i:mid + 1]
        else:
            arr[left + k:right + 1] = arr_tmp[j:right + 1]

        return s3_count


if __name__ == '__main__':
    input_arr = [13, 8, 10, 6, 15, 18, 12, 20, 9, 14, 17, 19]
    solution = Solution()
    output = solution.inversion_counting(input_arr, left=0, right=len(input_arr) - 1)
    print(output)
