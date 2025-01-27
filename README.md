# Artifact
This repository contains the artifacts for the paper _Unveiling Price Manipulation Attacks in Chainlink’s Decentralized Oracle Networks_. Specifically, these artifacts include the code for data collection, the datasets we used, our analysis scripts, and our experimental results. The requirements for running the program are listed in [requirements.txt](https://github.com/SecurityDON/Artifact/blob/main/requirements.txt).
- [./data_collection/](https://github.com/SecurityDON/Artifact/tree/main/data_collection). This directory is used to collect price observations from Chainlink's decentralized oracle networks. [fetch_all_pairs_price_observations.py](https://github.com/SecurityDON/Artifact/blob/main/data_collection/fetch_all_pairs_price_observations.py) provides a general framework for collecting price observations for all pairs, while [fetch_eth_usd_price_observations.py](https://github.com/SecurityDON/Artifact/blob/main/data_collection/fetch_eth_usd_price_observations.py) is specifically designed for collecting ETH/USD price observations.
- [./analysis_scripts/](https://github.com/SecurityDON/Artifact/tree/main/analysis_scripts). This directory is used for data analysis. Specifically, their functions are as follows.
  - [success_probability_of_attacks.py](https://github.com/SecurityDON/Artifact/blob/main/analysis_scripts/success_probability_of_attacks.py) calculates the theoretical success probability of _non-leader attack_.
  - [index_dev_distribution.py](https://github.com/SecurityDON/Artifact/blob/main/analysis_scripts/index_dev_distribution.py) calculates the expected value of index deviation caused by the attacks and the corresponding distribution.
  - [all_observations_discrepancy.py](https://github.com/SecurityDON/Artifact/blob/main/analysis_scripts/all_observations_discrepancy.py) calculates the discrepancy between the maximum and minimum values of a historical observations list.
  -  [honest_discrepancy.py](https://github.com/SecurityDON/Artifact/blob/main/analysis_scripts/honest_discrepancy.py) calculates the lower bound of the honest discrepancy.
  -  [attack_simulation.py](https://github.com/SecurityDON/Artifact/blob/main/analysis_scripts/attack_simulation.py) simulates the price bias caused by our proposed attacks.
  -  [long_term_attack_ens_case.py](https://github.com/SecurityDON/Artifact/blob/main/analysis_scripts/long_term_attack_ens_case.py)calculates the accumulated profits resulting from long-term attacks using the ENS case.
