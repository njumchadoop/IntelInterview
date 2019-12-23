def solution(N, K):
    """
    :param N: floor
    :param K: eggs
    :return: eggs needed number找到是那一层鸡蛋被砸碎的临界层
    思路: 第i层扔鸡蛋,那么会出现两种情况
    situation 1: 鸡蛋碎了,那么鸡蛋只剩下K - 1个鸡蛋,楼层区间只剩下i - 1层
    situation 2: 鸡蛋没碎,那么鸡蛋还是有K个，但是楼层区间则变为(i + 1) - N层
    构建一个二维数组,[k][m]表示k个鸡蛋在m次测试内能测出最大的楼层数L: 那么k和m为0时,该矩阵的数组第一行第一列全部为0
    而当K为1的时候,即有[1][m] = m
    即这个数组矩阵的大小应该是0 0 0  ... 0   (最大长度为K+1,因为只给了限定的K个鸡蛋)
                            0 1
                            0 2
                            . .
                            . .
                            . .
                            0 m
                            测试次数长度为m,矩阵中每一个值为能够测出的鸡蛋摔碎的最大楼层
    那么问题就转变为使用K个鸡蛋测试m次,求使得[K][m] >= N的最小m值
    """
    res = [[0 for j in range(K + 1)] for i in range(N + 1)]
    res[0][0] = 0
    for m in range(1, N + 1):  # 1<= m <= N
        res[m][0] = 0
        for k in range(1, K + 1):  # 1<= k <= K
            # 假如在第X层测试,就会有两种情况发生
            # 鸡蛋碎
            # 鸡蛋没有碎
            res[m][k] = res[m - 1][k] + res[m - 1][k - 1] + 1
            print("res[%s][%s] is %s" % (m, k, res[m][k]))
            if res[m][k] >= N:
                return m
    return N


if __name__ == '__main__':
    # 时间复杂度 N * K,空间复杂度N * K
    print(solution(10, 3))