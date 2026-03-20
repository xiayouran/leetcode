# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-20 17:49
# Filename: huffman.py
from typing import List, Tuple
import heapq


class HuffmanNode:
    """霍夫曼树节点"""
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char          # 字符（叶子节点有效）
        self.freq = freq          # 频率
        self.left = left          # 左子节点
        self.right = right        # 右子节点

    # 为了让堆能比较节点，定义小于比较（按频率）
    def __lt__(self, other):
        return self.freq < other.freq


class Solution:
    def __init__(self):
        self.codes = {}     # 字符 -> 编码字典

    def huffman(self, F: List[Tuple[str, int]]):
        """
        时间复杂度为O(nlogn)
        """
        F = sorted(F, key=lambda x: x[0], reverse=False)

        heap = [HuffmanNode(char=ch, freq=freq) for ch, freq in F]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)    # 最小频率节点
            y = heapq.heappop(heap)    # 次小频率节点
            # 合并为新节点，频率为两者之和
            z = HuffmanNode(freq=x.freq + y.freq, left=x, right=y)
            heapq.heappush(heap, z)

        return heap[0]     # 树根（堆顶）

    def encode(self, node, current_code: str = ""):
        """递归遍历树，生成编码表"""
        if node is None:
            return

        # 叶子节点：保存字符的编码
        if node.char:
            self.codes[node.char] = current_code
            return

        # 非叶子：向左加'0'，向右加'1'
        self.encode(node.left, current_code + "0")
        self.encode(node.right, current_code + "1")

if __name__ == '__main__':
    F = [('a', 45), ('b', 13), ('c', 12), ('d', 16), ('e', 9), ('f', 5)]
    solution = Solution()
    root = solution.huffman(F)
    solution.encode(root)

    for ch, freq in F:
        print(f'{ch}: {solution.codes[ch]}')
