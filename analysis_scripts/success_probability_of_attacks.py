import math
from decimal import Decimal, ROUND_HALF_UP


# The probability of a successful attack when x oracles conceal
def P_success_conceal(l, x):
    i_ori = math.floor(l / 2)
    k_range = max(l - 1 - i_ori, i_ori)
    total_combs = math.comb(l, x)
    p_k_sum = Decimal(0)
    expectation = Decimal(0)
    P_success = Decimal(0)
    for k in range(0, k_range + 1):
        pos_k_y = math.floor(l / 2) - math.floor((l - x) / 2) + k
        neg_k_y = math.floor(l / 2) - math.floor((l - x) / 2) - k
        if 0 <= pos_k_y <= x:
            pos_k_i_man = math.floor((l - x) / 2) + pos_k_y
            pos_k_lcombs = math.comb(pos_k_i_man, pos_k_y)
            pos_k_rcombs = math.comb(l - 1 - pos_k_i_man, x - pos_k_y)
            pos_k_combs = pos_k_lcombs * pos_k_rcombs
            pos_k_p = Decimal(pos_k_combs) / Decimal(total_combs)
            pos_k_p = pos_k_p.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
        else:
            pos_k_p = Decimal(0)
        if 0 <= neg_k_y <= x:
            neg_k_i_man = math.floor((l - x) / 2) + neg_k_y
            neg_k_lcombs = math.comb(neg_k_i_man, neg_k_y)
            neg_k_rcombs = math.comb(l - 1 - neg_k_i_man, x - neg_k_y)
            neg_k_combs = neg_k_lcombs * neg_k_rcombs
            neg_k_p = Decimal(neg_k_combs) / Decimal(total_combs)
            neg_k_p = neg_k_p.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
        else:
            neg_k_p = Decimal(0)
        if k == 0:
            p_k = pos_k_p
            P_success = Decimal(1) - p_k
        else:
            p_k = pos_k_p + neg_k_p
        p_k_sum = p_k_sum + p_k
        expectation = expectation + Decimal(k) * p_k
    return P_success


def P_success_non_leader_deflation(l, x):
    i_ori = math.floor(l / 2)
    k_range = x
    total_combs = math.comb(l, x)
    p_k_sum = Decimal(0)
    expectation = Decimal(0)
    P_success = Decimal(0)
    for k in range(0, k_range + 1):
        z = x - k
        i_man = math.floor(l / 2) - x + z
        lcombs = math.comb(i_man, z)
        rcombs = math.comb(l - 1 - i_man, x - z)
        combs = lcombs * rcombs
        p_k = Decimal(combs) / Decimal(total_combs)
        p_k = p_k.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
        p_k_sum = p_k_sum + p_k
        expectation = expectation + Decimal(k) * p_k
        if k == 0:
            P_success = Decimal(1) - p_k
    return P_success


def P_success_non_leader_inflation(l, x):
    i_ori = math.floor(l / 2)
    k_range = x
    total_combs = math.comb(l, x)
    p_k_sum = Decimal(0)
    expectation = Decimal(0)
    P_success = Decimal(0)
    for k in range(0, k_range + 1):
        z = k
        i_man = math.floor(l / 2) + z
        lcombs = math.comb(i_man, z)
        rcombs = math.comb(l - 1 - i_man, x - z)
        combs = lcombs * rcombs
        p_k = Decimal(combs) / Decimal(total_combs)
        p_k = p_k.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
        p_k_sum = p_k_sum + p_k
        expectation = expectation + Decimal(k) * p_k
        if k == 0:
            P_success = Decimal(1) - p_k
    return P_success
