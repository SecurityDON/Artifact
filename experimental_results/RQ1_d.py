from analysis_scripts.all_observations_discrepancy import *
import pandas as pd


df_obs = pd.read_csv("../data/EthUsdObsWithTime.csv")
df_obs.loc[:, "d"] = df_obs.apply(min_max_d, axis=1)
pct_list = [0.99998, 0.9999, 0.999, 0.99, 0.9, 0]
calculate_distribution(pct_list, df_obs["d"])
