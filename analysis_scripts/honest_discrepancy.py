import pandas as pd
from decimal import Decimal, ROUND_HALF_UP


def lower_bound(row, f):
    gaps = []
    for i in range(f + 1):
        start_cols = "ob" + str(i)
        end_cols = "ob" + str(i + 2 * f)
        if pd.isna(row[end_cols]) or pd.isna(row[start_cols]):
            break
        else:
            gap_value = row[end_cols] - row[start_cols]
            gaps.append(gap_value)
    min_gaps = min(gaps)
    return min_gaps


def calculate_ratio(row, col_1, col_2):
    # str_median = str(row['median'])
    # str_col = str(row[col])
    str_col_1 = str(row[col_1])
    str_col_2 = str(row[col_2])
    div_tmp_1 = Decimal(str_col_1) / Decimal(str_col_2)
    div_tmp_2 = div_tmp_1.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    div_final_r = float(div_tmp_2)
    return div_final_r