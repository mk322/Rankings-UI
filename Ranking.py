import pandas as pd
from sympy import re
import numpy as np


class rankings:
    def __init__(self, file_path, op_path, other_paths):
        self.df = pd.read_csv(file_path, header=0, index_col=0)
        self.op = pd.read_csv(op_path, header=0, index_col=0)
        self.rating_names = list(other_paths.keys())
        self.ratings = {}
        for rate_name in other_paths.keys():
            self.ratings[rate_name] = pd.read_csv(other_paths[rate_name], header=0, index_col=0)

    def get_columns(self):
        return list(self.df.index)

    def get_num_rows(self):
        return len(self.df.columns)

    def get_vertical_rankings(self):
        columns = list(self.df.columns)
        rows = list(self.df.index)
        ret_list = [ [] for _ in range(len(columns)) ]
        for i in range(len(rows)):
            ordered_list = list(self.df.iloc[i].sort_values(ascending=True).index)
            for j in range(len(ordered_list)):
                ret_list[j].append(ordered_list[j])
        return ret_list

    def get_all_rankings(self):
        rows = list(self.df.index)
        ret_list = []
        for i in range(len(rows)):
            ordered_list = list(self.df.iloc[i].sort_values(ascending=True).index)
            ret_list.append(ordered_list)
        return ret_list

    def get_op_rankings(self):
        ret = {}
        rows = list(self.op.index)
        props = list(self.op.columns)
        maxi = 0
        for reviewer in rows:
            ret[reviewer] = {}
            for prop in props:
                rate = self.op.loc[reviewer, prop]
                if not np.isnan(rate):
                    if rate not in ret[reviewer]:
                        ret[reviewer][rate] = [prop]
                    else:
                        ret[reviewer][rate].append(prop)
                        if len(ret[reviewer][rate]) > maxi:
                            maxi = len(ret[reviewer][rate])
        return ret, maxi

    def get_fq_rating(self, reviewer, prop):
        return self.ratings["FQ"].loc[reviewer, prop]