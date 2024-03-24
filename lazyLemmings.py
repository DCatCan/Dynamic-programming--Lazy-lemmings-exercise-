import math
import matplotlib.pyplot as plt

import sys
sys.setrecursionlimit(1500)


N = [x for x in range(1, 51)] + [100*x for x in range(1, 6)] + [1000]
l = [x for x in range(1, 11)]


mem = [[math.inf for x in range(1001)] for y in range(11)]

# Naive recursive approact


def jump(N, l):
    if N == 0 or N == 1:
        return N
    if l == 1:
        return N
    minTrials = math.inf

    for k in range(1, N+1):
        results = max(jump(N-k, l), jump(k-1, l-1))
        if results < minTrials:
            minTrials = results
    return 1 + minTrials

# recusive memory approach


def memoJump(N, l):
    if mem[l][N] != math.inf:
        return mem[l][N]

    if N == 0 or N == 1:
        return N
    if l == 1:
        return N

    minTrials = math.inf

    for k in range(1, N+1):
        results = max(memoJump(N-k, l), memoJump(k-1, l-1))
        if results < minTrials:
            minTrials = results
    mem[l][N] = 1 + minTrials
    return 1 + minTrials


def main():
    # print(l)
    # print(N)

    enlista = []
    # for i in l:
    #     temp = []
    #     for j in N:
    #         mem = [[math.inf for x in range(1001)] for y in range(11)]
    memoJump(100, 2)
    for i in range(1, 103):
        print(str(i) + " : " + str(mem[2][i]), end=" | \n")

    #         temp.append(memoJump(j, i))
    #     enlista.append(temp)

    # for i in range(1, 10):
    #     yval = enlista[i]
    #     print(yval)
    #     plt.plot(N, yval, label="l = " + str(i+1))

    # plt.xlabel("N - values")
    # plt.ylabel("min trials")
    # plt.title("trials for different l and N inputs")
    # plt.legend()
    # plt.show()


if __name__ == "__main__":
    main()
