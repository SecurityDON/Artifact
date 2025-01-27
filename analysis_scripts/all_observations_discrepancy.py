from decimal import Decimal, ROUND_HALF_UP
import numpy as np


def exact_divide(op_1, op_2, str_dec):
    div_tmp_1 = Decimal(op_1) / Decimal(op_2)
    div_tmp_2 = div_tmp_1.quantize(Decimal(str_dec), rounding=ROUND_HALF_UP)
    div_final_r = float(div_tmp_2)
    return div_final_r


def min_max_d(row):
    obs_len = int(row["obs_len"])
    last_ob_num = obs_len - 1
    max_col = "ob" + str(last_ob_num)
    min_col = "ob0"
    median_col = "median"
    min_max_desc = row[max_col] - row[min_col]
    str_min_max_desc = str(min_max_desc)
    str_median = str(row[median_col])
    d = exact_divide(str_min_max_desc, str_median, "0.000001")
    return d


def calculate_distribution(pct_list, df_col):
    for p in pct_list:
        value = np.percentile(df_col, p * 100)
        print(f"{(1.0 - p) * 100}    {value}")