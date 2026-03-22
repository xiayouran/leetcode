# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-21 12:31
# Filename: depth_first_search.py
"""
辅助数组：
color：表示顶点的状态
 - White：白色顶点u尚未被发现，发现后直接入队
 - Black：黑色顶点u已被处理，无需再次入队
 - Gray：灰色顶点已经入队，无需再次入队
pred：记录顶点u的前驱节点pred[u]
d：顶点发现时刻（变为灰色的时刻）
f：顶点完成时刻（变为黑色时刻）
"""
from typing import List, Dict


class Solution:
    def DFS(self, graph: Dict[str, List[str]]) -> None:
        """
        时间复杂度为O(V+E)
        """
        # self.d = {}
        # self.f = {}

        self.color = {}
        # self.pred = {}
        for u, _ in graph.items():
            self.color[u] = 'White'
            # self.pred[u] = None

        # self.time = 0
        for v, _ in graph.items():
            if self.color[v] == 'White':
                self.DFS_Visit(graph, v=v)

    def DFS_Visit(self, graph: Dict[str, List[str]], v: str):
        self.color[v] = 'Gray'
        # self.time += 1
        # self.d[v] = self.time   # 记录发现时刻

        print(v)

        for w in graph[v]:
            if self.color[w] == 'White':
                # self.pred[w] = v
                self.DFS_Visit(graph, v=w)

        self.color[v] = 'Black'
        # self.time += 1
        # self.f[v] = self.time   # 记录结束时刻


if __name__ == '__main__':
    graph = {
        '1': ['2', '5'],
        '2': ['1', '6'],
        '3': ['6', '7', '4'],
        '4': ['3', '7', '8'],
        '5': ['1'],
        '6': ['2', '3', '7'],
        '7': ['6', '3', '4', '8'],
        '8': ['7', '4'],
    }
    solution = Solution()
    solution.DFS(graph=graph)
