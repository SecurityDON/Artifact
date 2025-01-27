import math
import pandas as pd
import numpy as np
from matplotlib import ticker
import matplotlib.pyplot as plt
import matplotlib


def plotting(fig_x, fig_y, y_space, y_label):
    matplotlib.use('TkAgg')
    plt.rcParams['font.family'] = 'Arial'
    plt.figure(figsize=(5, 4.5), dpi=150)
    # fig_x = df_filter_2["blockNumber"]
    # df_filter_2["utc_time"] = pd.to_datetime(df_filter_2["utc_time"], format='mixed', errors='coerce')
    # fig_x = df_filter_2["utc_time"]
    # fig_y = df_filter_2["max_deviation_prop"]
    f2_color = (240 / 255, 148 / 255, 150 / 255)
    plt.scatter(fig_x, fig_y, color=f2_color, s=10, marker='o', alpha=0.8)
    plt.xlim([fig_x.min(), fig_x.max()])
    plt.ylim([min(fig_y), max(fig_y) + y_space])
    # plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.0f}'.format(x)))
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=65))
    plt.xticks(rotation=90)
    plt.tick_params(axis='both', direction='in', labelsize=9)
    plt.xlabel('block number', fontsize=12)
    plt.ylabel('D_ext' + y_label, fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()


def calculate_distribution(column):
    percentiles = np.arange(0.1, 1.01, 0.1)
    ranges = {}
    for p in percentiles:
        value = np.percentile(column, p * 100)
        ranges[f"{p * 100}%"] = value
    return ranges


if __name__ == "__main__":
    num_oracles = 31
    f = math.floor(num_oracles / 3)
    df = pd.read_csv("../data/EthUsdObsWithTime.csv")
    min_upper_bound = f
    hmin_upper_bound = "ob" + str(f)
    # hmax_lower_bound = 2 * f
    hmax_lower_bound = "ob" + str(2 * f)
    df_filter_1 = df.loc[df["obs_len"] == num_oracles].copy()
    col_min = "ob0"
    col_max = "ob" + str(num_oracles - 1)
    df_filter_1.loc[:, "ext_dev_min"] = df_filter_1.loc[:, hmin_upper_bound] - df_filter_1.loc[:, col_min]
    df_filter_1.loc[:, "ext_dev_max"] = df_filter_1.loc[:, col_max] - df_filter_1.loc[:, hmax_lower_bound]
    df_filter_1.loc[:, "D_ext_min"] = df_filter_1.loc[:, "ext_dev_min"] / df_filter_1.loc[:, "median"]
    df_filter_1.loc[:, "D_ext_max"] = df_filter_1.loc[:, "ext_dev_max"] / df_filter_1.loc[:, "median"]
    num_rmv = math.floor(0.001 * len(df_filter_1))
    idx_top_min_deviation = df_filter_1.nlargest(num_rmv, 'D_ext_min', keep='all').index
    idx_top_max_deviation = df_filter_1.nlargest(4, 'D_ext_max', keep='all').index
    idx_top_deviation = idx_top_min_deviation.union(idx_top_max_deviation)
    df_filter_2 = df_filter_1.drop(index=idx_top_deviation)
    df_filter_2 = df_filter_2.reset_index(drop=True)
    df_filtered = df_filter_2.drop(columns=["ext_dev_min", "ext_dev_max", "D_ext_min", "D_ext_max"])
    # df_filtered.to_csv("../data/FilteredEthUsdObs.csv", index=False)
    # The following two figures are the D_ext before filtering
    plotting(df_filter_1["blockNumber"], df_filter_1["D_ext_min"], 0.03, "(minimum)")
    plotting(df_filter_1["blockNumber"], df_filter_1["D_ext_max"], 200000, "(maximum)")
    # The following two figures are the D_ext after filtering
    plotting(df_filter_2["blockNumber"], df_filter_2["D_ext_min"], 0.03, "(minimum)")
    plotting(df_filter_2["blockNumber"], df_filter_2["D_ext_max"], 0.005, "(maximum)")
    D_ext_min_distribution = calculate_distribution(df_filter_2["D_ext_min"])
    D_ext_max_distribution = calculate_distribution(df_filter_2["D_ext_max"])
    print(f"The following is D_ext_min_distribution")
    for key, value in D_ext_min_distribution.items():
        print(f"{key}  {value}")
    print()
    print(f"The following is D_ext_max_distribution")
    for key, value in D_ext_max_distribution.items():
        print(f"{key}  {value}")
    print(df_filter_2['D_ext_min'].max())
    print(df_filter_2['D_ext_max'].max())
