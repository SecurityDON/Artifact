from analysis_scripts.attack_simulation import *


def non_leader_attack_results(l_ori_data, num_oracle, pct_list):
    r_inflation = non_leader_attack_inflation(l_ori_data, num_oracle)
    print("The following is the result under inflation case")
    print_distribution(pct_list, r_inflation["p_inflt_r"], r_inflation["p_inflt"])
    r_deflation = non_leader_attack_deflation(l_ori_data, num_oracle)
    print("The following is the result under deflation case")
    print_distribution(pct_list, r_deflation["p_deflt_r"], r_deflation["p_deflt"])


def leader_driven_attack_results(l_ori_data, num_oracle, pct_list):
    r_inflation = leader_driven_attack_inflation(l_ori_data, num_oracle)
    print("The following is the result under inflation case")
    print_distribution(pct_list, r_inflation["p_inflt_r"], r_inflation["p_inflt"])
    r_deflation = leader_driven_attack_deflation(l_ori_data, num_oracle)
    print("The following is the result under deflation case")
    print_distribution(pct_list, r_deflation["p_deflt_r"], r_deflation["p_deflt"])


if __name__ == "__main__":
    l_ori_file = "../data/FilteredEthUsdObs.csv"
    num_eth_usd_oracles = 31
    percentiles = [0.99995, 0.9999, 0.999, 0.99, 0.9, 0.01]
    # Remove the comment symbols of next line when reproducing
    # non_leader_attack_results(l_ori_file, num_eth_usd_oracles, percentiles)
    leader_driven_attack_results(l_ori_file, num_eth_usd_oracles, percentiles)