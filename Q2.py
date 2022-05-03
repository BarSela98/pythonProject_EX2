import pandas as pd


# Q2.1
def three_x_plus_1(s):
    lst = s.tolist()
    lst = [x * 0.5 if x % 2 == 0 else (x * 3) + 1 for x in lst]
    return pd.Series(lst, s.index)


# Q2.2
# check if prints well. makes series with new indexes and original data.
def reindex_up_down(s):
    lst = s.index.toList()
    lst = [x.upper if x[0].isupper() else x.lower() for x in lst]
    return pd.series(s.toList(), lst)


# Q2.3
def no_nans_idx(s):
    return pd.notnull(s)


# Q2.4
def partial_sum(s):
    return math.sqrt(s.sum())


# Q2.5
# empty
def partial_eq(s1, s2):
    temp = [True if x == y else False for x, y in zip(s1.tolist(), s2.tolist())]
    return pd.Series(temp, s1.index)


# Q2.6
def dropna_mta_style(df, how='any'):
    df.dropna(0, how)
    df.dropna(1, how)
    return df


# Q2.7
def get_n_largest(df, n=0, how='col'):
    if how == 'row':
        df = df.transpose()
        df = df.sort_values(by=[0])
    else:
        df = df.sort_values(by=['col1'])
    return df.iloc[n]


# Q2.8
def unique_dict(df, how='col'):
    return df.drop_duplicates(subset=[''])


# Q2.9
def upper(df):
    df = df.apply(lambda s: s.astype(str).str.upper())
    return df
