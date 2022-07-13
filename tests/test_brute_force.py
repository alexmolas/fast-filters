import pandas as pd

from fast_filters.brute_force import brute_force_not_null_intersection, brute_force_c2_contains_c1


def test_brute_force_not_null_intersection():
    df = pd.DataFrame({"a": [[1, 2, 3], [4, 5, 6]], "b": [[1, 5], [4]]})
    assert all(brute_force_not_null_intersection(df, 'a', 'b') == pd.Series([True, True]))

    df = pd.DataFrame({"a": [[1, 2, 3], [4, 5, 6]], "b": [[4], [1]]})
    assert all(brute_force_not_null_intersection(df, 'a', 'b') == pd.Series([False, False]))


def test_brute_force_c2_contains_c1():
    df = pd.DataFrame({"a": [[1, 2, 3], [4, 5, 6]], "b": [[1], [4]]})
    all(brute_force_c2_contains_c1(df, 'a', 'b') == pd.Series([True, True]))

    df = pd.DataFrame({"a": [[1, 2, 3], [4, 5, 6]], "b": [[1, 5], [4]]})
    all(brute_force_c2_contains_c1(df, 'a', 'b') == pd.Series([False, True]))
