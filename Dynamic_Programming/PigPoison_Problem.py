import math


def solution(N, T, t):
    """
    Pig  will die in t after pig drinks a bottle of poisonous water and there is limited time T
    :param N: The number of bottles of water
    :param T: The limited time
    :param t: The limited time and T is x times of t
    :return: the number of pigs that test the poisonous water
    有N只猪,只有一瓶水有毒,使用最少的猪在规定T时间内测出那瓶有毒的水,
    猪可以无线喝水有毒立刻死亡,但是喝完要等t分钟内才能继续喝水
    所以每次喝完水,必须要等t时间才能让猪继续喝水,水是否有毒.本题以T为一小时,t为15分钟算
    当猪只有一只的时候,一只猪只能测T/t次即4次,即一只猪只能一小时测5瓶水
    当猪2有只得时候,每只猪可以测5瓶水,使用交叉测法,水形成一个5 * 5的方阵,一只猪测行,一只猪测列,喝瓶水的混合水,则可以在1小时内测25瓶水
    当小猪数量为3时,那么就是3维的5*5*5矩阵交叉测试,那么可以测125瓶水
    """
    times = T / t + 1
    res = math.ceil(math.log(N, times))  # 向上取整    PS:math.floor向下取整
    return res


if __name__ == '__main__':
    print(solution(625, 60, 15))
