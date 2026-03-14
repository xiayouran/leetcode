# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-14 17:26
# Filename: merge_sort.py
from typing import List
import copy


class Solution:
    def merge_sort(self, arr: List[int], left: int, right: int) -> List[int]:
        """
        归并排序时间复杂度分析：
        运行次数函数T(n)= 2T(n/2) + O(n)
        时间复杂度为O(nlogn)
        """
        if left == right:  # 只有一个元素，直接返回
            return [arr[left]]
        if left > right:  # 空区间
            return []

        mid = (left + right) // 2
        self.merge_sort(arr, left, mid)         # T(n/2)
        self.merge_sort(arr, mid + 1, right)    # T(n/2)
        self.merge(arr, left, mid, right)       # O(n)

        return arr[left:right+1]

    def merge(self, arr: List[int], left: int, mid: int, right: int) -> List[int]:
        arr_tmp = copy.deepcopy(arr)
        i, j, k = left, mid + 1, 0      # k为最终输出有序数组的索引
        while i <= mid and j <= right:
            if arr_tmp[i] <= arr_tmp[j]:
                arr[left + k] = arr_tmp[i]    # 小的放前面
                i += 1
            else:
                arr[left + k] = arr_tmp[j]
                j += 1
            k += 1

        # 处理剩余部分
        # 两块排好序的子数组，一块已经全部放入，另一块的剩余部分直接放入
        if i <= mid:
            arr[left + k:right + 1] = arr_tmp[i:mid + 1]
        else:
            arr[left + k:right + 1] = arr_tmp[j:right + 1]

        return arr[left:right + 1]



if __name__ == '__main__':
    input_arr = [32, 15, 11, 26, 53, 87, 3, 61]
    solution = Solution()
    output = solution.merge_sort(input_arr, left=0, right=len(input_arr) - 1)
    print(output)
