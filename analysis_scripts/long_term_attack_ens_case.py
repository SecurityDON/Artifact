import math
import pandas as pd
import numpy as np
from eth_abi import decode
from decimal import Decimal, ROUND_HALF_UP
from analysis_scripts.index_dev_distribution import *


def is_string(value):
    return isinstance(value, str)


def checkCall(df):
    df_filtered = df[df["input"].str.startswith("0x50e9a715")]
    df_filtered.reset_index(drop=True, inplace=True)
    return df_filtered


def decodeOutput(row):
    try:
        raw_rt = row["output"]
        decode_rt = decode(["uint256"], bytes.fromhex(raw_rt[2:]))
        rt = decode_rt[0]
        return rt
    except Exception as e:
        return np.nan


# col_name is equivalent to the col_tp_man parameter in the following function
def matchPriceFeed(num_oracle, df_obs, df_trace, attack_dev, col_name):
    idx_dev = math.floor(attack_dev)
    for i in df_obs.index:
        p = df_obs.at[i, "median"]
        idx_median = math.floor(num_oracle / 2)
        man_deflt = "ob" + str(idx_median - idx_dev)
        # tp denotes the total price
        tp_man = df_obs.at[i, man_deflt]
        amplify = 10 ** 8
        p = int(p * amplify)
        tp_man = int(tp_man * amplify)
        cur_block = df_obs.at[i, "blockNumber"]
        next_block = df_obs.at[i, "next_feed_block"]
        df_trace.loc[(df_trace["block_number"] >= cur_block) & (df_trace["block_number"] < next_block), ["p", col_name]] = [p, tp_man]
    return df_trace


def profitCalculate(row, col_tp_man, col_return):
    price = int(row["p"])
    tprice_man = int(row[col_tp_man])
    rt_wei = int(row[col_return])
    ratio = Decimal(price) / Decimal(tprice_man)
    profit_ratio = ratio - Decimal(1)
    profit_wei = Decimal(rt_wei) * profit_ratio
    profit_eth = profit_wei / Decimal(10 ** 18)
    profit_eth = profit_eth.quantize(Decimal("0.00000000000000001"), rounding=ROUND_HALF_UP)
    return profit_eth


def non_leader_accumulated_profits(obs_data_path, traces_data_path, num_oracle, f):
    df_obs = pd.read_csv(obs_data_path)
    df_trace = pd.read_csv(traces_data_path)
    df_trace = df_trace[df_trace['output'].apply(is_string)]
    df_trace.reset_index(drop=True, inplace=True)
    df_obs = df_obs[df_obs["blockNumber"] >= 14678295]
    df_obs.reset_index(drop=True, inplace=True)
    df_trace = df_trace[df_trace["block_number"] < 21111711]
    df_trace.reset_index(drop=True, inplace=True)
    df_trace = checkCall(df_trace)
    df_trace["return_wei"] = df_trace.apply(decodeOutput, axis=1)
    df_trace.dropna(inplace=True)
    attack_idx_dev = index_dev_nonleader_deflation(num_oracle, f)
    df_non_leader = matchPriceFeed(num_oracle, df_obs, df_trace, attack_idx_dev, "price_man")
    df_non_leader.dropna(inplace=True)
    df_non_leader.reset_index(drop=True, inplace=True)
    df_non_leader["profit_eth"] = df_non_leader.apply(profitCalculate, axis=1, args=("price_man", "return_wei"))
    accumulated_profits = df_non_leader["profit_eth"].sum()
    return accumulated_profits


def leader_driven_accumulated_profits(obs_data_path, traces_data_path, num_oracle, f):
    df_obs = pd.read_csv(obs_data_path)
    df_trace = pd.read_csv(traces_data_path)
    df_trace = df_trace[df_trace['output'].apply(is_string)]
    df_trace.reset_index(drop=True, inplace=True)
    df_obs = df_obs[df_obs["blockNumber"] >= 14678295]
    df_obs.reset_index(drop=True, inplace=True)
    df_trace = df_trace[df_trace["block_number"] < 21111711]
    df_trace.reset_index(drop=True, inplace=True)
    df_trace = checkCall(df_trace)
    df_trace["return_wei"] = df_trace.apply(decodeOutput, axis=1)
    df_trace.dropna(inplace=True)
    attack_idx_dev = index_dev_leader_driven_deflation(num_oracle, f)
    df_leader_driven = matchPriceFeed(num_oracle, df_obs, df_trace, attack_idx_dev, "price_man")
    df_leader_driven.dropna(inplace=True)
    df_leader_driven.reset_index(drop=True, inplace=True)
    df_leader_driven["profit_eth"] = df_leader_driven.apply(profitCalculate, axis=1, args=("price_man", "return_wei"))
    accumulated_profits = df_leader_driven["profit_eth"].sum()
    return accumulated_profits