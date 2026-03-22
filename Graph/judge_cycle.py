# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    youran.xia@foxmail.com
# Datetime: 2026-03-21 14:50
# Filename: judge_cycle.py
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
    def DFS_judge_cycle(self, directed_graph: Dict[str, List[str]]) -> bool:
        """
        时间复杂度为O(V+E)
        """
        self.color = {}
        self.pred = {}
        for u, _ in directed_graph.items():
            self.color[u] = 'White'
            self.pred[u] = None

        for v, _ in directed_graph.items():
            if self.color[v] == 'White':
                if self.DFS_Visit_judge_cycle(directed_graph, v=v):
                    return True
        return False

    def DFS_Visit_judge_cycle(self, directed_graph: Dict[str, List[str]], v: str) -> bool:
        self.color[v] = 'Gray'
        for w in directed_graph[v]:
            if self.color[w] == 'Gray':     # 存在后代到祖先的后向边
                return True                 # 存在环路
            if self.color[w] == 'White':
                self.pred[w] = v
                if self.DFS_Visit_judge_cycle(directed_graph, v=w):
                    return True
        self.color[v] = 'Black'
        return False


if __name__ == '__main__':
    directed_graph = {
        '1': ['2'],
        '2': ['4'],
        '3': ['1'],
        '4': ['5'],
        '5': ['3'],
    }
    solution = Solution()
    output = solution.DFS_judge_cycle(directed_graph=directed_graph)
    print(output)
