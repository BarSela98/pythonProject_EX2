import pandas as pd


# Q2.1
def three_x_plus_1(s):
    lst = s.toList()
    [x / 2 if x % 2 else (3 * x + 1) for x in lst]
    return pd.series(lst, s.index)


# Q2.2
# check if prints well. makes series with new indexes and original data.
def reindex_up_down(s):
    lst = s.index.toList()
    lst = [x.upper if x[0].isupper else x.lower for x in lst]
    return pd.series(s.data, lst)


# Q2.3
def no_nans_idx(s):
    return pd.notnull(s)


# Q2.4
def partial_sum(s):
    return math.sqrt(s.sum())


# Q2.5
# empty
def partial_eq(s1, s2):
    #what is inters??


# Q2.6
# check if for 'any' its correct. need to drop col and row.
# check if the arg is right
def dropna_mta_style(df, how=’any’):
    df.dropna(0, how)
    df.dropna(1, how)
    return df


# Q2.7
def get_n_largest(df, n=0, how=’col’):




# Q2.8
def unique_dict(df, how=’col’):


# Q2.9
# Q2.10