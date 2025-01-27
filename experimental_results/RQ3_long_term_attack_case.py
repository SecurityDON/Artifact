import pandas as pd
import numpy as np
from analysis_scripts.long_term_attack_ens_case import *
from analysis_scripts.index_dev_distribution import *
import math


# The price observations data file is FilteredEthUsdObs.csv, https://github.com/SecurityDON/Artifact/blob/main/data/FilteredEthUsdObs.csv
obs_data_path = "your storage path for price observations data"
# The traces data file used below is too large, and due to anonymity requirements, we are unable to share it via our cloud storage links. When the anonymity restrictions are lifted, we will share this portion of data.
traces_data_path = "your storage path for traces data"
num_oracle = 31
f = math.floor(num_oracle / 3)
non_leader_r = non_leader_accumulated_profits(obs_data_path, traces_data_path, num_oracle, f)
leader_driven_r = leader_driven_accumulated_profits(obs_data_path, traces_data_path, num_oracle, f)
print(f"The accumulated profits caused by non-leader attacks is {non_leader_r} ETH")
print(f"The accumulated profits caused by leader-driven attacks is {leader_driven_r} ETH")
