# Artifact
This repository contains the artifacts for the paper _Unveiling Price Manipulation Attacks in Chainlink’s Decentralized Oracle Networks_. Specifically, these artifacts include the code for data collection, the datasets we used, our analysis scripts, and our experimental results. The requirements for running the program are listed in [requirements.txt](https://github.com/SecurityDON/Artifact/blob/main/requirements.txt).
- [./data_collection/](https://github.com/SecurityDON/Artifact/tree/main/data_collection). This directory is used to collect price observations from Chainlink's decentralized oracle networks. _fetch_all_pairs_price_observations.py_ provides a general framework for collecting price observations for all pairs, while _fetch_eth_usd_price_observations.py_ is specifically designed for collecting ETH/USD price observations.
- [./analysis_scripts/](https://github.com/SecurityDON/Artifact/tree/main/analysis_scripts). This directory is used for data analysis. Specifically, their functions are as follows.
  - _success_probability_of_attacks.py_ calculates the theoretical success probability of our proposed attacks.
  - _index_dev_distribution.py_ calculates the expected value of index deviation caused by the attacks and the corresponding distribution.
  - _all_observations_discrepancy.py_ calculates the discrepancy between the maximum and minimum values of a historical observations list.
  -  _honest_discrepancy.py_ calculates the lower bound of the honest discrepancy.
