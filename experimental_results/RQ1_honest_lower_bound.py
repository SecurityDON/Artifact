from analysis_scripts.honest_discrepancy import *
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import ticker


df_obs = pd.read_csv("../data/EthUsdObsWithTime.csv")
df_obs.loc[:, "honest_lower_bound"] = df_obs.apply(lower_bound, axis=1, args=(10,))
df_obs.loc[:, "ratio"] = df_obs.apply(calculate_ratio, axis=1, args=("honest_lower_bound", "median"))
matplotlib.use('TkAgg')
plt.rcParams['font.family'] = 'Arial'
scatter_color = (246 / 255, 99 / 255, 28 / 255)
plt.figure(figsize=(5, 4), dpi=150)
fig_x = df_obs['blockNumber']
fig_y = df_obs["ratio"]
plt.scatter(fig_x, fig_y, color=scatter_color, s=10, marker='o', alpha=0.7)
plt.xlim([min(fig_x), max(fig_x)])
print(min(fig_x), max(fig_x))
plt.ylim([min(fig_y), max(fig_y) + 0.001])
plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=15))
plt.xticks(rotation=30)
plt.tick_params(axis='both', direction='in', labelsize=16)
plt.xlabel('block number', fontsize=16)
plt.ylabel('discrepancy lower bound', fontsize=16)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()