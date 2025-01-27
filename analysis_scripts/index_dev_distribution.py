import math
from decimal import Decimal, ROUND_HALF_UP


def index_dev_concealment(l, x):
    i_ori = math.floor(l / 2)
    k_range = max(l - 1 - i_ori, i_ori)
    total_combs = math.comb(l, x)
    p_k_sum = Decimal(0)
    expectation = Decimal(0)
    if l % 2 == 1 and x % 2 == 0:
        for k in range(0, k_range + 1):
            pos_k_y = int(x / 2) + k
            neg_k_y = int(x / 2) - k
            # Since x is an even number, pos_k_y + neg_k_y = x, the condition can be set as follows
            if pos_k_y > x or neg_k_y > x:
                break
            pos_k_i_man = math.floor((l - x) / 2) + pos_k_y
            neg_k_i_man = math.floor((l - x) / 2) + neg_k_y
            pos_k_lcombs = math.comb(pos_k_i_man, pos_k_y)
            neg_k_lcombs = math.comb(neg_k_i_man, neg_k_y)
            pos_k_rcombs = math.comb(l - 1 - pos_k_i_man, x - pos_k_y)
            neg_k_rcombs = math.comb(l - 1 - neg_k_i_man, x - neg_k_y)
            pos_k_combs = pos_k_lcombs * pos_k_rcombs
            neg_k_combs = neg_k_lcombs * neg_k_rcombs
            pos_k_p = Decimal(pos_k_combs) / Decimal(total_combs)
            pos_k_p = pos_k_p.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
            neg_k_p = Decimal(neg_k_combs) / Decimal(total_combs)
            neg_k_p = neg_k_p.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
            if k == 0:
                p_k = pos_k_p
            else:
                p_k = pos_k_p + neg_k_p
            # print(f"k = {k}")
            # print(f"pos_k_y = {pos_k_y}, neg_k_y = {neg_k_y}")
            # print(f"p_k = {p_k}")
            # print()
            p_k_sum = p_k_sum + p_k
            expectation = expectation + Decimal(k) * p_k
        # print(f"p_k_sum = {p_k_sum}")
        # print(f"expectation = {expectation}")
        # print()
    elif l % 2 == 0 and x % 2 == 1:
        for k in range(0, k_range + 1):
            pos_k_y = int((x + 1) / 2) + k
            neg_k_y = int((x + 1) / 2) - k
            # if pos_k_y > x or neg_k_y > x:
            #     break
            # pos_k_i_man = math.floor((l - x) / 2) + pos_k_y
            # neg_k_i_man = math.floor((l - x) / 2) + neg_k_y
            # pos_k_lcombs = math.comb(pos_k_i_man, pos_k_y)
            # neg_k_lcombs = math.comb(neg_k_i_man, neg_k_y)
            # pos_k_rcombs = math.comb(l - 1 - pos_k_i_man, x - pos_k_y)
            # neg_k_rcombs = math.comb(l - 1 - neg_k_i_man, x - neg_k_y)
            # pos_k_combs = pos_k_lcombs * pos_k_rcombs
            # neg_k_combs = neg_k_lcombs * neg_k_rcombs
            # pos_k_p = Decimal(pos_k_combs) / Decimal(total_combs)
            # pos_k_p = pos_k_p.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
            # neg_k_p = Decimal(neg_k_combs) / Decimal(total_combs)
            # neg_k_p = neg_k_p.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
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
            else:
                p_k = pos_k_p + neg_k_p
            # print(f"k = {k}")
            # print(f"pos_k_y = {pos_k_y}, neg_k_y = {neg_k_y}")
            # print(f"pos_k_p = {pos_k_p}, neg_k_p = {neg_k_p}")
            # print(f"p_k = {p_k}")
            # print()
            p_k_sum = p_k_sum + p_k
            expectation = expectation + Decimal(k) * p_k
        # print(f"p_k_sum = {p_k_sum}")
        # print(f"expectation = {expectation}")
        # print()
    return expectation


def index_dev_nonleader_deflation(l, x):
    i_ori = math.floor(l / 2)
    k_range = x
    total_combs = math.comb(l, x)
    p_k_sum = Decimal(0)
    expectation = Decimal(0)
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
    #     print(f"k = {k}")
    #     print(f"z = {z}")
    #     print(f"p_k = {p_k}")
    #     print()
    # print(f"p_k_sum = {p_k_sum}")
    # print(f"expectation = {expectation}")
    # print()
    return expectation


def index_dev_nonleader_inflation(l, x):
    i_ori = math.floor(l / 2)
    k_range = x
    total_combs = math.comb(l, x)
    p_k_sum = Decimal(0)
    expectation = Decimal(0)
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
    #     print(f"k = {k}")
    #     print(f"z = {z}")
    #     print(f"p_k = {p_k}")
    #     print()
    # print(f"p_k_sum = {p_k_sum}")
    # print(f"expectation = {expectation}")
    # print()
    return expectation


def index_dev_leader_driven_inflation(l, x):
    f = int((l - 1) / 3)
    i_ori = math.floor(l / 2)
    u_range = x
    total_combs = math.comb(l, x)
    p_k_sum = Decimal(0)
    expectation = Decimal(0)
    for u in range(0, u_range + 1):
        i_man = u + l - f - 1
        lcombs = math.comb(i_man, u)
        rcombs = math.comb(l - 1 - i_man, x - u)
        combs = lcombs * rcombs
        p_k = Decimal(combs) / Decimal(total_combs)
        p_k = p_k.quantize(Decimal("0.000000001"), rounding=ROUND_HALF_UP)
        k = u + f - math.floor((f + 1) / 2)
        p_k_sum = p_k_sum + p_k
        expectation = expectation + Decimal(k) * p_k
    return expectation


def index_dev_leader_driven_deflation(l, x):
    f = int((l - 1) / 3)
    i_ori = math.floor(l / 2)
    u_range = x
    total_combs = math.comb(l, x)
    p_k_sum = Decimal(0)
    expectation = Decimal(0)
    for u in range(0, u_range + 1):
        i_man = u - x + f
        lcombs = math.comb(i_man, u)
        rcombs = math.comb(l - 1 - i_man, x - u)
        combs = lcombs * rcombs
        p_k = Decimal(combs) / Decimal(total_combs)
        p_k = p_k.quantize(Decimal("0.000000001"), rounding=ROUND_HALF_UP)
        k = x + math.floor((f + 1) / 2) - u
        p_k_sum = p_k_sum + p_k
        expectation = expectation + Decimal(k) * p_k
    return expectation