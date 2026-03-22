# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-21 15:27
# Filename: topological_sort.py
"""
辅助数组：
color：表示顶点的状态
 - White：白色顶点u尚未被发现，发现后直接入队
 - Black：黑色顶点u已被处理，无需再次入队
 - Gray：灰色顶点已经入队，无需再次入队
pred：记录顶点u的前驱节点pred[u]
"""
from typing import List, Dict
from collections import deque, defaultdict


class Solution:
    def topological_sort_BFS(self, directed_graph: Dict[str, List[str]]) -> None:
        """
        时间复杂度为O(V+E)
        """
        # 计算每个节点的入度
        in_degree = defaultdict(int)
        for node in directed_graph:
            in_degree[node] = in_degree.get(node, 0)  # 确保节点在入度表中
            for neighbor in directed_graph[node]:
                in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

        Q = deque()
        for v, _ in directed_graph.items():
            if in_degree[v] == 0:
                Q.append(v)     # 入度为0的节点入队

        while Q:
            u = Q.popleft()
            print(u)

            for v in directed_graph[u]:
                in_degree[v] -= 1   # 前驱节点出队，当前节点的入度-1
                if in_degree[v] == 0:
                    Q.append(v)

    def topological_sort_DFS(self, directed_graph: Dict[str, List[str]]) -> List[str]:
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
        '短裤': ['长裤', '鞋'],
        '长裤': ['腰带', '鞋'],
        '腰带': ['外套'],
        '衬衫': ['腰带', '领带'],
        '领带': ['外套'],
        '外套': [],
        '袜子': ['鞋'],
        '鞋': [],
        '手表': [],
    }
    solution = Solution()
    # solution.topological_sort_BFS(directed_graph=directed_graph)

    output = solution.topological_sort_DFS(directed_graph)
    output.reverse()    # 逆序，最后完成的先输出

    print(output)
