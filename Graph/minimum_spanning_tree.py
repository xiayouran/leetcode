# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-21 17:23
# Filename: minimum_spanning_tree.py
"""
辅助数组：
color：表示顶点的状态
 - Black：黑色顶点u已选择，u in V_A
 - White：白色顶点u未被选择，u in V-V_A
dist：记录横跨(V_A, V-V_A)边的权重
 - 顶点集V_A到顶点u的最短距离，dist[u] = min(w(x,u)), x in V_A
 - 轻边：min(dist[u]), u in V-V_A
pred：记录顶点u的前驱节点pred[u]
 - (pred[u], u)为最小生成树的边
"""
from typing import List, Dict
import math


class Solution:
    def MST_Prim(self, graph: Dict[str, List[str]], s: str):
        """
        时间复杂度为O(V+E)
        """
        self.color = {}
        self.dist = {}
        self.pred = {}
        for u, _ in graph.items():
            self.color[u] = 'White'
            self.dist[u] = math.inf
            self.pred[u] = None

        self.dist[s] = 0    # 选择顶点s作为起点
        for v, _ in graph.items():  # 依次添加其他顶点
            min_dist = math.inf     # 记录权值最小值
            rec = s     # 记录安全边的端点 加入边(u,v)还是最小生成树，则边(u,v)为安全边
            for w, _ in graph.items():      # V_A中的一个顶点与V-V_A多个顶点选最小的边
                if self.color[w] == 'White' and self.dist[w] < min_dist:    # 记录新增的安全边
                    min_dist = self.dist[w]
                    rec = w
            for (u, weight) in graph[rec]:  # 更新dist数组（V_A中可能有多个顶点与顶点u相连，选择最小的边）
                if weight < self.dist[u]:
                    self.dist[u] = weight
                    self.pred[u] = rec
            self.color[rec] = 'Black'


if __name__ == '__main__':
    graph = {
        'a': [('b', 4), ('h', 8)],
        'b': [('a', 4), ('h', 1), ('c', 8)],
        'c': [('b', 8), ('i', 2), ('f', 4), ('d', 7)],
        'd': [('c', 7), ('f', 14), ('z', 9)],
        'f': [('g', 2), ('c', 4), ('d', 14), ('z', 10)],
        'g': [('h', 1), ('i', 4), ('f', 2)],
        'h': [('a', 8), ('b', 1), ('i', 7), ('g', 1)],
        'i': [('h', 7), ('g', 4), ('c', 2)],
        'z': [('d', 9), ('f', 10)],
    }
    solution = Solution()
    solution.MST_Prim(graph=graph, s='a')
