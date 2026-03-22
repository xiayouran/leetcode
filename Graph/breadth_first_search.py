# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-21 11:25
# Filename: breadth_first_search.py
"""
辅助数组：
color：表示顶点的状态
 - White：白色顶点u尚未被发现，发现后直接入队
 - Black：黑色顶点u已被处理，无需再次入队
 - Gray：灰色顶点已经入队，无需再次入队
pred：记录顶点u的前驱节点pred[u]
dist：源点s到顶点u的距离dist[u]
"""
from typing import List, Dict
from collections import deque
import math


class Solution:
    def BFS(self, graph: Dict[str, List[str]], s: str) -> None:
        """
        时间复杂度为O(V+E)
        """
        Q = deque()     # 初始化队列

        color = {}
        # pred = {}
        # dist = {}
        for u, _ in graph.items():
            color[u] = 'White'
            # pred[u] = None
            # dist[u] = math.inf

        Q.append(s)     # 源点s入队
        color[s] = 'Gray'
        # dist[s] = 0

        while Q:
            u = Q.popleft()
            print(u)
            for v in graph[u]:
                if color[v] == 'White':
                    color[v] = 'Gray'
                    # dist[v] = dist[u] + 1   # s->v的距离 = s->u的距离+1
                    # pred[v] = u
                    Q.append(v)
            color[u] = 'Black'


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
    solution.BFS(graph=graph, s='2')
