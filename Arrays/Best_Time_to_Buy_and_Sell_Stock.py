# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Best_Time_to_Buy_and_Sell_Stock.py                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ytouate <ytouate@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/06 12:26:17 by ytouate           #+#    #+#              #
#    Updated: 2022/04/06 13:49:57 by ytouate          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        max_p = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(profit, max_p)
            else:
                l = r
            r += 1
        return (max_p)
