# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-21 16:21
# Filename: strongly_connected_components.py
"""
辅助数组：
color：表示顶点的状态
 - White：白色顶点u尚未被发现，发现后直接入队
 - Black：黑色顶点u已被处理，无需再次入队
 - Gray：灰色顶点已经入队，无需再次入队
pred：记录顶点u的前驱节点pred[u]
"""
from typing import List, Dict


class Solution:
    def strongly_connected_components(self, directed_graph: Dict[str, List[str]]):
        """
        时间复杂度为O(V+E)
        """
        # Step1: 构造反向图
        reverse_directed_graph = {node: [] for node in directed_graph}
        for u, neighbors in directed_graph.items():
            for v in neighbors:
                reverse_directed_graph[v].append(u)

        # Step2: 在反向图上执行DFS，得到按顶点完成时刻的顺序L
        L = self.DFS(reverse_directed_graph)

        # Step3: 在原始图上按L逆序执行DFS，得到强连通分量
        self.color = {}
        for v, _ in directed_graph.items():
            self.color[v] = 'White'
        L.reverse()
        R = []
        for u in L:
            if self.color[u] == 'White':
                L_scc = self.DFS_Visit(directed_graph, v=u)
                R.append(L_scc)
        return R

    def DFS(self, directed_graph: Dict[str, List[str]]) -> List[str]:
        """
        时间复杂度为O(V+E)
        """
        self.color = {}
        for v, _ in directed_graph.items():
            self.color[v] = 'White'
        L = []
        for v, _ in directed_graph.items():
            if self.color[v] == 'White':
                L_prime = self.DFS_Visit(directed_graph, v=v)
                L.extend(L_prime)
        return L

    def DFS_Visit(self, directed_graph: Dict[str, List[str]], v: str) -> List[str]:
        self.color[v] = 'Gray'

        L = []
        for w in directed_graph[v]:
            if self.color[w] == 'White':
                L_prime = self.DFS_Visit(directed_graph, v=w)
                L.extend(L_prime)

        self.color[v] = 'Black'
        L.append(v)

        return L


if __name__ == '__main__':
    directed_graph = {
        '1': ['3', '10'],
        '2': ['6'],
        '3': ['4', '7'],
        '4': ['1', '6'],
        '5': ['2'],
        '6': ['5'],
        '7': ['7'],
        '8': ['9', '10'],
        '9': ['7', '8'],
        '10': ['1'],
    }
    solution = Solution()
    output = solution.strongly_connected_components(directed_graph=directed_graph)
    print(output)
