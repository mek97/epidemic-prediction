import math

import numpy as np
from scipy import stats


class AverageAlgorithms:
    """
    Average Model Class
    """

    @staticmethod
    def get_exp_wtd_avg(time_series, column_name, params=None):
        if params is None:
            params = {}
        std = params.get("std", 2.5)
        a = params.get("a", 1)
        r = params.get("r", 0.3)

        if len(time_series) == 0:
            # Returning -1 due to no data
            return -1

        # Outlier Removal
        time_series_filtered = time_series[(np.abs(stats.zscore(time_series[column_name])) < std)]

        if len(time_series_filtered) == 0:
            # Data not sufficient fall back to original time series
            time_series_filtered = time_series

        exp_wtd_average = 0
        wtd_sum = 0
        ctr = len(time_series_filtered) - 1
        for _, val in time_series_filtered[column_name].iteritems():
            wtd = a * (r ** ctr)
            wtd_sum += wtd
            exp_wtd_average += wtd * val
            ctr -= 1

        exp_wtd_average /= wtd_sum
        exp_wtd_average = math.ceil(exp_wtd_average)
        return exp_wtd_average
