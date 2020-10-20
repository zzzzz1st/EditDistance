import numpy as np


def editDistDP(str1, str2, m, n):
    cost = np.zeros((m + 1, n + 1))
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                cost[i, j] = j
            elif j == 0:
                cost[i, j] = i
            elif str1[i - 1] == str2[j - 1]:
                cost[i, j] = cost[i - 1, j - 1]
            else:
                cost[i, j] = 1 + min(cost[i, j - 1], cost[i - 1, j], cost[i - 1, j - 1])
    return cost[m, n]