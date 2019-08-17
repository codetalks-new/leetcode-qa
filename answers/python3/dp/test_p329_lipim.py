# coding: utf-8

__author__ = '代码会说话'
"""
329. 矩阵中的最长递增路径

给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
输出: 4 
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
输出: 4 
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from functools import lru_cache

class Solution:
  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    M = matrix
    R = len(matrix)
    if not R:
      return 0
    C = len(matrix[0])
    def is_valid_pos(r:int,c:int):
      return (r > -1 and r < R) and (c > -1 and c < C)

    @lru_cache(maxsize=None)
    def walk(r:int,c:int):
      prev = M[r][c]
      # 上下左右
      next_len = 0
      for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr = r + dr
        nc = c + dc
        if is_valid_pos(nr,nc):
          num =M[nr][nc]
          if not (num > prev):
            continue
          nl = 1+walk(nr,nc)
          next_len  = max(nl,next_len)
      return next_len

    max_len = 1
    for r in range(R):
      for c in range(C):
        path_len = 1+  walk(r,c)
        max_len = max(path_len, max_len)
    return max_len









def test():
  s = Solution()

  assert s.longestIncreasingPath([
    [7,8,9],
    [9,7,6],
    [7,2,3]]) == 6

  assert s.longestIncreasingPath([
    [4,4,5],
    [3,7,6],
    [2,2,1]
  ] ) == 4
  assert s.longestIncreasingPath([[1]]) == 1
  assert s.longestIncreasingPath([]) == 0

  assert s.longestIncreasingPath([
    [9,9,4],
    [6,6,8],
    [2,1,1]
  ] ) == 4

  assert s.longestIncreasingPath([
    [3,4,5],
    [3,2,6],
    [2,2,1]
  ] ) == 4
  assert s.longestIncreasingPath([
    [1,1,1],
    [1,1,1],
    [1,1,1]
  ] ) == 1

  assert s.longestIncreasingPath([
    [1,1,1],
    [1,1,1],
    [1,2,1]
  ] ) == 2


  largeArr = [[16,4,16,0,17,5,16,13,19,6,15,3,15,7,9,7,9,9,7,6,18,0,17,19,3,9,0,3,11,19,11,13,3,5,17,4,4,17,10,8,5,17,12,13,12,18,16,0,16,2,6,9,10,7,10,14,4,10,1,13,2,6,16,9,12,0,19,3],[1,12,15,0,11,0,10,12,11,17,12,1,16,0,16,18,16,2,8,12,15,11,6,6,17,2,11,13,3,10,6,18,18,18,15,4,4,9,18,12,15,4,8,8,12,6,1,16,9,15,3,3,12,6,6,13,12,12,1,7,1,6,18,5,8,18,6,12],[13,6,12,8,2,3,12,19,1,5,12,4,13,4,19,12,6,14,18,7,3,5,8,13,17,12,18,3,11,13,12,12,1,15,7,12,14,2,4,0,2,7,6,13,16,14,12,16,17,12,10,19,6,6,18,18,4,16,6,0,15,15,10,0,0,2,16,1],[8,4,13,10,3,2,14,8,14,13,7,10,13,2,13,18,17,2,6,13,5,15,16,2,8,8,6,8,19,13,3,11,17,10,13,0,13,14,1,5,19,5,11,13,0,14,8,16,3,7,4,16,5,4,10,18,13,3,18,8,5,11,7,1,11,16,10,4],[3,1,3,11,6,1,11,11,7,12,7,12,18,11,4,10,7,7,8,18,12,18,9,1,11,12,13,16,11,1,7,5,18,13,12,2,5,2,13,6,12,14,1,10,8,8,7,14,15,16,8,10,8,3,11,9,8,9,9,11,17,3,8,19,13,9,19,3],[2,16,1,4,18,14,7,15,15,14,15,14,10,12,12,17,4,7,4,17,9,9,14,3,12,4,1,18,0,1,9,13,15,19,5,16,2,15,17,10,1,11,2,13,3,2,12,12,17,17,1,17,4,16,13,3,14,5,18,17,4,10,17,1,18,2,10,14],[15,17,10,4,7,1,3,15,11,10,14,6,8,11,8,1,8,19,10,12,10,13,12,10,17,15,12,11,16,3,9,17,5,17,7,17,9,9,2,12,1,13,12,4,19,7,7,14,18,13,4,17,19,10,9,0,5,16,18,2,14,12,1,11,13,2,7,8],[15,19,7,16,13,6,2,13,19,14,9,10,13,10,0,15,15,10,19,3,18,14,15,7,6,5,10,7,3,8,8,14,13,19,3,7,16,1,14,10,16,11,2,18,6,6,1,1,16,2,17,15,16,12,2,13,1,4,16,13,13,12,12,10,3,4,16,1],[9,2,14,7,2,12,14,19,7,2,5,4,15,14,19,4,14,10,12,13,14,3,3,13,13,13,3,13,8,8,16,18,17,10,6,7,9,11,5,19,11,5,14,8,4,10,17,18,4,8,8,14,11,4,7,15,7,3,14,14,2,9,18,18,19,4,19,2],[16,17,12,12,15,15,4,8,16,9,16,17,15,3,3,8,11,1,17,3,14,18,1,17,12,3,18,13,7,0,13,5,17,14,18,16,10,16,4,12,1,4,6,13,18,14,13,9,1,18,8,5,18,11,4,0,1,8,4,3,6,19,12,12,19,10,6,9],[9,9,14,13,19,11,17,3,9,5,5,3,3,1,4,5,12,4,2,17,10,10,8,16,7,8,15,18,17,0,18,1,11,5,6,7,12,2,0,1,17,0,4,6,3,8,9,3,19,0,12,4,8,14,7,4,7,11,7,15,0,17,5,14,16,12,15,9],[11,0,15,0,18,0,14,19,15,0,7,7,4,8,5,6,5,12,15,4,1,4,8,0,5,9,12,18,13,19,6,19,3,15,18,12,10,4,2,5,13,13,6,9,10,6,10,18,6,8,18,18,5,4,5,1,14,4,17,15,13,9,18,7,2,5,5,13],[15,1,1,13,6,15,3,17,17,13,7,17,7,9,15,19,16,10,11,9,16,2,6,4,12,18,4,10,18,11,17,8,5,13,3,2,18,13,0,7,10,9,16,15,8,9,18,8,1,2,5,13,3,14,13,16,11,7,12,2,13,0,1,19,11,18,19,13],[5,0,19,19,4,7,8,7,8,2,15,11,13,1,4,0,11,5,4,1,18,10,17,7,1,18,12,7,17,19,6,14,3,8,11,18,4,14,16,1,5,5,15,13,11,18,12,15,11,15,18,14,12,5,1,17,3,7,12,17,4,5,4,12,15,17,16,18],[17,10,3,14,2,1,4,15,3,17,1,9,9,8,16,7,1,8,1,14,11,16,0,15,7,2,0,4,7,19,3,8,19,3,2,14,18,4,0,11,18,6,6,11,8,11,0,11,13,5,16,13,13,5,9,3,3,0,19,5,5,5,10,13,3,18,9,4],[10,16,10,15,16,10,11,9,19,17,15,16,13,18,16,16,17,13,13,19,11,3,13,11,19,8,19,3,12,14,19,0,11,2,18,17,15,0,14,10,3,6,18,1,9,6,10,11,15,5,18,1,19,5,13,8,19,0,8,7,11,7,17,8,15,13,4,19],[1,4,5,18,5,2,0,10,16,10,1,7,14,14,15,3,12,0,12,9,14,13,3,2,11,18,15,9,7,15,4,11,6,7,1,2,11,1,5,19,2,4,2,19,12,2,7,11,5,11,14,8,5,18,11,14,12,14,0,6,7,14,3,11,13,19,1,9],[2,6,17,0,8,10,1,8,19,13,9,11,15,19,2,17,6,17,13,17,15,7,5,8,15,3,19,13,6,2,18,4,6,18,4,13,13,0,17,2,5,13,6,5,1,11,13,16,2,12,7,5,19,1,2,10,3,2,14,3,6,4,4,19,11,13,3,14],[5,0,19,0,8,8,15,8,19,11,14,19,17,19,19,0,17,9,14,14,14,3,19,4,16,15,6,5,9,7,13,11,5,4,11,11,13,7,1,19,10,19,15,1,2,0,11,16,16,18,18,8,2,1,14,15,16,5,13,3,4,19,9,4,4,3,0,6],[16,18,10,8,9,11,17,4,3,9,17,3,0,12,18,13,10,9,15,14,15,1,9,0,15,11,5,5,19,13,3,9,9,4,4,2,9,0,7,4,11,11,0,16,6,4,17,0,1,11,15,0,5,12,13,1,8,17,0,10,5,3,12,10,0,3,6,13],[5,5,15,2,5,14,12,14,5,4,12,18,4,7,12,13,8,1,2,9,9,9,7,16,18,12,10,2,17,9,8,5,1,3,6,18,11,2,10,19,10,11,15,3,8,5,0,9,11,12,0,17,16,5,8,9,15,16,2,8,4,3,3,13,10,16,15,11],[19,11,8,6,8,14,17,2,11,16,10,11,3,1,14,12,15,15,8,2,0,0,4,9,8,0,13,19,0,14,4,13,14,0,16,19,0,15,15,11,10,1,2,13,14,17,9,15,3,5,8,7,11,15,7,4,3,10,8,2,13,1,14,13,16,6,12,17],[5,9,5,15,9,4,0,6,4,7,1,13,12,9,11,1,14,13,4,15,11,19,18,6,19,19,8,3,13,17,2,18,15,12,18,10,4,8,13,2,3,19,9,11,6,19,13,18,1,18,18,6,13,8,1,15,2,10,16,14,1,16,2,17,11,16,11,7],[7,11,15,13,5,13,6,12,13,5,18,15,19,3,2,10,6,17,1,9,5,17,11,11,12,13,10,14,12,18,19,15,9,3,0,7,6,6,16,13,13,1,3,5,0,15,8,2,8,10,4,4,12,0,0,9,6,2,3,17,18,9,4,9,16,5,19,12],[1,1,14,2,2,8,6,14,13,2,8,15,4,10,15,16,0,4,12,17,10,8,10,6,18,1,0,6,14,17,8,0,6,14,9,2,3,18,9,16,9,0,13,13,10,6,7,13,16,12,7,6,14,7,10,17,12,3,3,9,13,15,11,16,18,2,1,1],[10,3,7,13,8,2,12,15,6,2,6,12,0,16,8,9,9,14,2,6,10,10,14,15,3,18,0,2,9,4,17,4,1,14,0,11,15,11,4,9,8,14,10,7,13,5,12,13,10,7,0,17,18,10,9,15,17,19,12,3,13,0,18,19,9,16,4,12],[14,11,19,1,3,9,6,11,15,17,3,3,14,4,16,6,0,4,16,6,4,14,17,3,0,6,11,9,11,5,3,2,16,7,6,12,13,5,3,0,12,2,12,6,13,14,12,1,19,18,2,7,14,7,13,2,18,19,17,15,13,5,5,8,5,10,4,8],[0,16,11,18,6,4,4,3,19,4,9,6,7,10,8,19,4,1,7,1,5,6,4,0,12,4,15,5,5,16,7,9,10,19,3,2,13,17,19,18,16,0,8,13,5,4,17,18,5,17,3,2,12,3,8,17,8,5,0,15,17,6,8,14,5,17,16,10],[16,7,4,2,4,0,12,3,12,2,18,19,15,19,17,14,12,3,16,1,17,1,16,1,17,18,2,8,6,0,5,15,19,10,16,15,3,17,13,10,17,2,3,6,1,11,18,6,15,0,5,1,18,4,11,2,15,14,18,10,5,14,2,6,19,16,7,6],[13,3,11,11,19,19,15,16,2,5,8,16,17,9,10,4,17,6,13,0,18,2,8,13,18,16,15,1,15,7,8,3,14,9,14,18,2,10,15,13,12,12,1,2,5,7,8,7,17,18,10,18,11,8,4,1,17,2,0,18,12,10,4,17,5,9,7,8],[3,17,7,0,9,13,8,18,15,16,7,1,17,1,11,0,0,2,13,4,14,11,2,15,17,13,7,0,4,1,4,3,9,15,19,10,15,4,5,1,0,19,14,19,11,3,6,2,1,11,11,13,5,13,11,10,14,5,16,6,1,14,3,8,13,1,10,14],[12,13,16,8,15,16,7,1,13,12,13,0,8,8,16,18,2,6,5,1,0,0,4,0,17,15,19,16,2,4,0,13,17,3,13,10,4,15,7,2,16,0,19,10,12,3,2,11,12,15,15,18,10,13,7,9,16,10,12,1,16,5,3,14,6,8,1,10],[12,13,1,2,8,18,12,4,18,18,2,17,1,11,1,19,9,9,0,6,6,9,14,9,4,19,9,18,15,18,2,2,19,13,11,18,17,19,13,18,4,13,7,0,11,0,3,14,8,18,16,14,7,17,2,14,13,15,10,4,12,6,18,16,3,3,14,10],[19,3,0,0,6,18,6,11,15,0,2,6,15,11,10,2,7,2,10,10,16,15,8,1,16,7,4,14,10,8,1,13,10,2,15,2,15,11,19,10,13,4,12,6,7,0,0,1,14,3,4,16,0,5,1,12,5,19,0,11,8,15,9,7,6,7,9,12],[15,7,1,15,18,16,19,8,19,18,15,17,16,18,11,19,14,17,13,10,6,0,2,7,4,4,10,1,2,11,1,10,19,14,17,11,8,19,14,15,0,7,2,6,12,13,3,1,16,13,10,19,18,3,3,5,6,16,19,3,8,10,18,12,18,9,15,12],[19,3,1,3,17,18,15,13,12,9,16,12,13,19,2,6,2,12,13,3,15,5,17,0,2,4,9,10,0,19,2,10,5,18,12,15,3,12,3,14,2,18,2,2,2,18,13,7,11,10,18,8,2,18,4,1,6,9,19,5,18,0,7,8,1,9,3,1],[8,11,9,4,4,15,2,2,5,10,1,7,7,18,1,16,4,4,11,17,10,8,1,15,15,5,17,11,3,8,3,4,15,14,19,3,0,1,18,8,18,4,8,18,15,17,2,3,16,16,19,17,15,6,1,5,12,1,18,3,14,2,10,4,9,13,18,16],[11,0,4,11,8,15,14,19,15,12,5,17,6,3,16,5,13,15,13,15,4,12,16,14,0,16,2,5,4,4,17,19,1,8,11,5,15,7,8,2,3,2,19,10,11,0,1,11,4,3,12,14,0,10,19,11,15,2,14,11,8,12,6,11,6,5,15,5],[16,9,18,16,11,18,2,18,6,8,15,2,8,18,6,8,7,0,0,16,12,4,10,14,12,12,10,13,6,14,5,15,2,12,12,13,14,7,12,5,12,10,17,16,17,3,0,3,5,17,7,9,7,10,18,10,16,17,0,8,8,12,15,19,10,8,17,4],[18,10,12,7,8,2,9,13,11,15,12,5,15,9,4,11,12,15,19,7,5,17,17,17,6,15,7,13,18,17,10,14,1,15,6,8,14,8,17,10,5,14,4,7,8,4,18,14,3,4,15,9,2,6,5,19,11,19,11,9,17,16,18,2,5,5,10,8],[19,17,17,3,9,8,15,10,8,7,6,1,16,1,12,16,7,7,7,15,2,4,13,15,9,19,15,5,12,9,0,11,6,19,18,19,17,16,9,1,8,17,15,4,19,14,17,9,17,9,8,16,1,1,8,11,10,1,14,15,7,12,17,5,16,17,8,6],[11,11,2,19,4,2,11,16,4,7,2,6,4,19,16,7,10,19,8,13,0,7,10,18,14,4,19,11,8,4,3,18,5,13,6,14,18,19,3,9,6,15,7,4,14,17,11,7,10,14,6,1,16,7,9,9,6,1,4,7,10,10,14,12,4,2,14,0],[4,11,10,18,19,11,12,7,10,7,8,1,1,18,0,3,10,12,0,10,8,1,7,6,15,2,14,18,4,17,8,15,10,14,14,8,13,15,10,0,13,10,7,9,15,6,4,8,0,18,18,9,3,2,8,16,2,4,14,8,13,4,6,14,19,1,12,14],[1,10,8,1,5,1,14,18,0,7,5,6,5,18,1,3,6,5,7,6,4,4,11,9,11,13,3,16,3,14,11,1,16,2,9,3,5,8,3,0,16,13,15,18,6,11,10,0,5,14,17,6,8,7,1,18,10,1,7,7,3,7,4,4,0,9,3,11],[6,15,2,16,19,4,18,8,17,13,4,19,15,8,0,18,18,8,0,7,5,11,14,14,14,12,19,8,6,0,1,11,15,11,4,6,12,4,2,1,10,4,1,4,6,17,6,4,19,8,11,14,10,1,12,9,17,3,7,0,18,11,0,13,13,7,13,9],[1,0,0,11,15,13,10,8,12,15,14,9,11,1,11,6,3,5,14,16,19,6,2,5,4,5,6,15,7,19,1,14,8,13,6,19,7,7,18,7,3,15,8,14,16,9,11,9,10,12,19,18,8,8,5,19,15,0,17,19,5,0,11,8,11,7,18,10],[19,2,6,16,17,9,12,17,12,16,12,11,5,10,6,17,13,6,3,5,5,14,11,11,4,17,12,15,16,2,19,6,9,11,14,0,3,0,18,12,11,12,6,9,13,10,13,12,17,6,10,7,17,4,2,17,7,14,0,9,16,13,13,5,13,1,1,18],[1,13,19,14,4,15,4,11,18,10,8,11,1,10,18,10,14,17,13,3,11,19,10,15,11,13,0,9,17,0,12,7,15,16,9,6,11,8,11,8,0,0,5,18,8,6,5,14,9,15,17,11,11,1,11,4,13,10,0,12,16,8,7,18,9,9,10,18],[5,7,3,16,7,1,13,9,15,12,5,10,3,4,8,16,19,11,14,18,14,16,10,16,7,18,5,16,6,12,13,17,5,17,8,8,11,1,5,16,0,18,10,14,18,17,0,9,4,5,1,13,18,7,9,15,8,5,3,13,4,12,14,10,11,1,1,8],[0,19,8,0,14,7,10,3,7,18,11,12,5,12,14,6,4,10,13,3,15,13,13,11,1,19,5,19,8,15,6,19,14,16,2,3,18,19,19,13,2,3,19,0,7,15,13,8,6,14,10,14,11,11,6,9,19,15,11,11,4,19,13,14,8,8,7,18],[6,15,13,19,7,3,19,1,9,10,3,16,2,3,0,11,16,1,19,17,16,8,14,14,2,10,8,8,16,19,15,1,6,2,18,6,2,7,3,2,4,17,16,14,14,1,7,13,19,14,0,3,10,8,12,7,18,3,15,2,0,17,14,4,5,8,4,17],[14,15,12,9,6,17,0,1,16,11,16,6,7,7,16,8,11,5,4,8,8,11,4,19,13,13,9,8,11,6,15,9,9,15,12,13,6,13,10,1,9,15,1,17,4,14,8,16,0,4,14,4,9,8,9,4,7,12,11,15,13,19,4,13,14,18,1,14],[5,1,3,11,10,3,12,6,15,14,3,14,5,13,18,11,5,12,2,0,18,14,16,10,14,11,19,10,4,1,1,8,17,10,2,11,13,0,4,1,3,19,19,19,2,8,5,9,2,10,16,12,6,7,8,5,14,6,0,12,16,8,2,11,2,6,12,4],[7,5,9,1,1,1,10,6,6,12,13,10,19,19,11,15,19,11,19,17,10,5,6,14,7,19,19,15,7,0,1,15,15,16,15,16,8,17,8,15,7,6,8,14,9,5,15,10,1,17,5,16,14,15,6,0,11,14,9,4,12,17,12,11,3,11,11,5],[9,18,14,12,16,18,13,13,2,2,7,5,0,14,15,8,12,4,12,3,13,8,14,2,6,15,14,13,6,11,3,4,11,16,16,10,12,16,0,11,14,14,12,7,19,10,19,19,7,0,11,19,13,3,16,9,12,4,7,8,7,15,17,17,10,16,14,4],[1,0,13,16,11,19,18,8,8,0,15,15,12,16,4,11,19,4,1,5,14,19,14,1,8,17,16,12,11,17,11,4,17,17,8,9,4,3,8,5,13,10,14,14,13,19,6,15,6,14,15,7,1,9,13,15,3,7,0,5,9,11,12,18,13,16,10,0],[2,9,7,2,12,6,12,6,9,9,18,4,0,0,5,1,5,16,13,3,18,2,9,4,17,15,16,7,13,5,5,6,3,18,6,14,19,9,17,1,1,3,8,2,0,9,4,0,16,15,13,8,7,14,7,1,2,19,4,18,13,16,7,15,3,16,7,18],[15,15,10,9,0,16,0,16,5,6,14,16,13,10,11,11,3,7,15,17,4,5,4,16,1,16,15,4,9,13,15,5,8,11,17,17,19,8,17,7,13,15,8,14,9,6,7,0,18,16,12,14,12,1,4,17,1,19,13,15,5,17,17,12,2,19,0,8],[9,8,0,18,14,16,15,8,2,6,7,10,16,7,1,1,9,9,11,8,17,11,5,17,3,10,19,2,1,9,18,4,18,18,8,14,17,4,18,19,7,14,1,13,13,14,16,18,19,15,18,5,13,0,4,15,17,14,10,16,1,6,19,12,19,8,18,10],[6,4,9,16,1,6,1,18,12,17,1,9,3,14,12,9,8,0,0,3,4,16,9,17,9,1,7,8,11,6,6,3,17,8,4,1,19,15,5,9,11,10,18,19,17,11,10,4,4,17,19,18,14,12,1,2,11,12,3,3,19,18,19,16,10,4,3,4],[10,8,19,1,16,19,16,14,8,5,12,5,7,13,4,13,18,7,18,18,14,1,17,19,2,6,10,10,9,0,7,15,9,14,7,11,13,9,12,15,12,12,9,8,2,14,15,10,5,16,0,18,5,1,3,7,8,9,7,8,6,7,2,0,12,19,2,14],[16,12,13,19,5,8,14,19,18,12,0,3,2,19,10,6,1,4,8,19,18,8,18,3,12,10,6,1,4,5,8,14,18,8,11,16,12,13,19,3,17,17,7,14,9,1,9,5,6,5,0,3,19,13,10,19,13,9,2,4,16,3,1,13,4,4,2,16],[9,16,19,7,16,15,17,13,11,9,16,19,13,6,15,7,8,10,19,19,11,8,10,7,17,2,12,0,16,2,2,13,15,4,19,16,7,3,12,11,4,19,12,13,12,1,13,7,12,7,19,3,12,6,6,4,10,12,14,2,15,4,11,17,18,10,3,1],[5,1,2,7,6,19,9,15,16,19,3,11,15,14,4,13,10,16,7,10,15,15,11,9,5,15,10,14,11,16,10,16,16,1,18,11,15,18,2,16,0,15,19,15,18,13,6,6,6,10,7,4,13,3,14,13,17,2,5,6,13,0,5,5,7,6,0,6],[15,3,0,0,14,7,11,7,17,19,15,12,12,12,12,12,3,18,4,15,17,2,2,4,8,14,4,17,9,13,16,11,13,14,15,13,1,5,14,19,18,8,1,7,8,14,17,1,2,10,12,2,4,12,0,11,9,12,6,15,0,14,3,12,13,19,14,12],[4,6,8,12,3,5,4,18,10,7,6,19,5,6,19,11,9,6,3,17,11,8,8,12,18,9,15,16,4,19,2,12,1,6,9,12,8,9,14,6,2,12,15,5,1,18,1,10,6,4,12,9,3,17,14,4,4,5,6,15,1,13,19,18,2,17,10,12],[12,0,8,18,0,1,4,9,16,19,6,10,17,12,13,6,12,7,15,6,11,16,11,5,9,9,4,1,0,6,13,0,3,19,9,11,3,18,2,6,13,0,9,7,15,4,16,10,19,3,12,10,1,8,2,18,15,8,10,18,16,6,16,12,10,5,15,12],[9,14,7,12,13,17,3,10,4,17,12,8,10,4,13,5,15,10,19,14,7,17,5,12,4,13,10,1,16,6,15,14,12,3,17,7,2,15,3,7,8,3,5,4,12,10,5,19,5,9,7,9,18,16,12,9,1,7,19,9,17,18,13,4,10,15,19,3],[8,5,14,5,11,14,11,6,6,18,17,11,10,19,16,15,15,17,4,1,15,15,3,14,6,6,16,11,1,10,9,4,14,19,4,17,9,9,10,9,7,15,13,6,8,2,16,8,11,5,9,5,9,11,2,14,14,13,5,11,10,10,19,14,12,9,0,18],[18,1,6,19,0,1,4,11,6,15,14,8,1,11,18,0,9,9,9,14,2,3,11,11,1,5,18,13,7,8,19,9,13,18,8,15,15,12,11,11,7,10,10,11,9,7,8,11,6,10,14,15,9,12,16,3,2,13,0,1,2,7,1,9,12,16,3,1],[15,13,17,5,5,10,12,1,0,10,10,6,15,1,11,7,4,9,14,12,5,0,19,6,13,14,18,3,6,6,7,1,17,2,15,2,10,9,8,14,5,19,6,16,6,4,11,8,6,5,17,14,14,14,2,17,5,13,1,10,6,6,0,3,8,2,5,17],[7,1,19,18,9,10,17,2,17,9,14,4,11,13,2,16,5,1,9,16,2,13,14,15,1,6,18,16,9,14,19,11,8,3,3,5,3,15,6,15,13,13,9,17,0,19,17,7,9,15,12,16,6,5,11,9,15,7,17,18,7,8,4,19,17,10,18,4],[19,11,7,3,2,12,6,14,16,17,18,10,16,13,19,13,4,2,18,1,0,4,14,6,18,11,1,14,10,4,19,5,2,5,9,4,12,17,15,14,16,14,4,10,8,3,19,16,13,10,15,3,4,15,3,12,7,15,1,8,3,15,6,5,19,13,7,11],[19,10,14,7,3,19,3,10,2,1,14,19,19,15,8,6,3,6,2,12,13,9,17,8,4,8,11,17,11,8,3,15,15,9,9,4,9,14,17,19,19,10,10,19,5,8,7,10,9,2,18,18,9,12,5,6,5,15,11,3,13,9,18,1,16,11,11,5],[7,1,8,12,9,11,2,1,4,18,16,8,10,3,15,3,18,0,8,11,9,12,12,0,6,16,11,0,6,15,8,17,0,4,17,10,1,16,10,7,19,11,1,8,10,0,18,13,8,13,12,7,14,2,4,13,12,5,16,2,8,19,17,14,13,5,11,8],[15,17,11,6,11,10,4,17,0,3,13,13,4,8,18,1,10,6,2,0,14,17,14,3,8,1,8,15,17,2,11,15,10,18,7,11,15,8,13,12,2,2,2,0,5,4,5,14,6,4,10,3,13,3,8,8,16,18,19,4,8,6,1,14,4,10,16,12],[15,2,18,4,2,10,7,4,0,17,7,1,15,12,0,16,7,19,19,12,1,6,5,5,19,10,4,6,0,2,0,7,0,17,8,10,1,10,14,3,8,4,16,19,3,1,0,17,8,10,7,0,16,16,10,14,9,16,5,11,13,18,9,11,5,0,6,1],[15,4,18,15,13,12,10,19,19,17,11,0,11,14,4,12,3,18,2,11,11,14,16,16,17,14,14,15,7,0,18,14,12,2,8,13,8,9,7,18,7,18,11,7,12,1,17,15,7,18,17,12,12,4,0,9,6,13,4,1,1,0,5,12,4,5,6,2],[8,15,0,7,14,5,10,1,12,7,2,9,4,17,4,9,4,16,10,3,2,8,1,3,11,0,15,12,19,13,5,17,18,3,12,11,6,9,7,1,2,14,13,3,10,6,5,14,8,16,14,18,15,3,7,15,6,12,15,17,9,5,18,1,5,8,12,5],[6,4,18,9,7,0,4,5,16,7,14,19,15,11,3,5,10,6,8,4,9,12,14,4,18,11,12,16,9,2,3,6,17,8,19,12,10,17,15,10,16,10,2,12,10,14,18,9,19,1,6,10,13,5,3,4,17,1,15,16,3,10,15,2,9,2,15,6],[3,7,12,7,16,4,5,1,12,11,3,9,18,3,4,16,13,14,3,10,16,8,3,11,19,18,6,0,4,6,16,3,11,4,9,11,14,13,11,2,6,12,17,18,3,17,14,8,18,0,2,10,13,0,5,12,3,1,0,0,15,19,8,18,1,11,14,7]]
  assert s.longestIncreasingPath(largeArr) == 9
