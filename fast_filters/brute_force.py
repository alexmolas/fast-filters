import pandas as pd


def brute_force_not_null_intersection(df: pd.DataFrame, c1: str, c2: str):
    def f(r):
        e1 = r[c1]
        e2 = r[c2]
        return len(set(e1) & set(e2)) != 0

    return df.apply(f, axis=1)


def brute_force_c2_contains_c1(df: pd.DataFrame, c1: str, c2: str):
    def f(r):
        e1 = r[c1]
        e2 = r[c2]
        return set(e2) == (set(e1) & set(e2))

    return df.apply(f, axis=1)
