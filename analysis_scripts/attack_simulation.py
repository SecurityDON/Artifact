from analysis_scripts.index_dev_distribution import *
import math
import pandas as pd
import numpy as np


def calculate_ratio(row, col):
    str_median = str(row['median'])
    str_col = str(row[col])
    div_tmp_1 = Decimal(str_col) / Decimal(str_median)
    div_tmp_2 = div_tmp_1.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    div_final_r = float(div_tmp_2)
    return div_final_r


def non_leader_attack_inflation(l_ori_data, num_oracle):
    f = math.floor(num_oracle / 3)
    i_ori = math.floor(num_oracle / 2)
    index_deviation_by_attack = index_dev_nonleader_inflation(num_oracle, f)
    index_deviation_for_simulation = math.floor(index_deviation_by_attack)
    str_i_man = "ob" + str(i_ori + index_deviation_for_simulation)
    df = pd.read_csv(l_ori_data)
    df["p_inflt"] = df.loc[:, str_i_man] - df.loc[:, "median"]
    df.loc[:, "current_block"] = df.loc[:, "blockNumber"]
    df.loc[:, "p_inflt_r"] = df.apply(calculate_ratio, axis=1, args=("p_inflt",))
    return df


def non_leader_attack_deflation(l_ori_data, num_oracle):
    f = math.floor(num_oracle / 3)
    i_ori = math.floor(num_oracle / 2)
    index_deviation_by_attack = index_dev_nonleader_deflation(num_oracle, f)
    index_deviation_for_simulation = math.floor(index_deviation_by_attack)
    str_i_man = "ob" + str(i_ori - index_deviation_for_simulation)
    df = pd.read_csv(l_ori_data)
    df["p_deflt"] = df.loc[:, "median"] - df.loc[:, str_i_man]
    df.loc[:, "current_block"] = df.loc[:, "blockNumber"]
    df.loc[:, "p_deflt_r"] = df.apply(calculate_ratio, axis=1, args=("p_deflt",))
    return df


def leader_driven_attack_inflation(l_ori_data, num_oracle):
    f = math.floor(num_oracle / 3)
    i_ori = math.floor(num_oracle / 2)
    index_deviation_by_attack = index_dev_leader_driven_inflation(num_oracle, f)
    index_deviation_for_simulation = math.floor(index_deviation_by_attack)
    str_i_man = "ob" + str(i_ori + index_deviation_for_simulation)
    df = pd.read_csv(l_ori_data)
    df["p_inflt"] = df.loc[:, str_i_man] - df.loc[:, "median"]
    df.loc[:, "current_block"] = df.loc[:, "blockNumber"]
    df.loc[:, "p_inflt_r"] = df.apply(calculate_ratio, axis=1, args=("p_inflt",))
    return df


def leader_driven_attack_deflation(l_ori_data, num_oracle):
    f = math.floor(num_oracle / 3)
    i_ori = math.floor(num_oracle / 2)
    index_deviation_by_attack = index_dev_leader_driven_deflation(num_oracle, f)
    index_deviation_for_simulation = math.floor(index_deviation_by_attack)
    str_i_man = "ob" + str(i_ori - index_deviation_for_simulation)
    df = pd.read_csv(l_ori_data)
    df["p_deflt"] = df.loc[:, "median"] - df.loc[:, str_i_man]
    df.loc[:, "current_block"] = df.loc[:, "blockNumber"]
    df.loc[:, "p_deflt_r"] = df.apply(calculate_ratio, axis=1, args=("p_deflt",))
    return df


def print_distribution(pct_list, df_col_ratio, df_col_price):
    for p in pct_list:
        r_bias = np.percentile(df_col_ratio, p * 100)
        p_bias = np.percentile(df_col_price, p * 100)
        print(f"{(1.0 - p) * 100}   {r_bias}   {p_bias}")
