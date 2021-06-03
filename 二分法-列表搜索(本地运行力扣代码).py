# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:01:21 2021

@author: chenty36


给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""

import time

def get_nums(nums,target):
    for i in nums:
        if i == target:
            return nums.index(i)
    else:
        return -1
    
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index,right_index = 0,len(nums) - 1
        # 为什么包含等于，因为等于的时候有意义，
        # 左闭又闭(一个是<=，一个是列表[a:b]取值是[a,b))
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2 #地板除(因为索引是从0开始的)
            if target > nums[middle_index]:
                left_index = middle_index + 1 #左闭又闭，middle_index已经取过了
            elif target < nums[middle_index]:
                right_index = middle_index - 1 #左闭又闭，middle_index已经取过了
            else:            #只剩下两值相等
                return middle_index
        return -1

#思路:
核心: 二分法思想
流程: 列表已是排好序的，用目标值与中间值进行比较，
目标值较大，则范围锁定到中间值与最大值的区间
以此类推
代码流程: 
先划定一个范围[left_index,right_index]
在这个范围内搜寻目标值，搜不到，退出，置为1 while循环,退出为1
循环里面，用目标值与中间值进行比较，目标值较大，则范围锁定到中间值与最大值的区间
       
    
nums = [-1,0,3,5,12]
target = 2
print(Solution().search(nums,target))
