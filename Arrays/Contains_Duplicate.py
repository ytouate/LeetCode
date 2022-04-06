# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Contains_Duplicate.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ytouate <ytouate@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/06 13:56:44 by ytouate           #+#    #+#              #
#    Updated: 2022/04/06 14:19:03 by ytouate          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution(object):

    def count(self, nums, i):
        count = 0
        for n in nums:
            if n == i:
                count += 1
        return count

    def is_sorted(self, nums):
        i, j = 0, 1
        while j < len (nums):
            if nums[i] > nums[j]:
                return False
            i += 1
            j += 1
        return True

    def containsDuplicate(self, nums):
        if self.is_sorted(nums):
            return False
        for i in nums:
            if self.count(nums, i) > 1:
                return True
        return False
