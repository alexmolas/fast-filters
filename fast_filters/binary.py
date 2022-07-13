from typing import Set

import pandas as pd


class Converter:
    def __init__(self, vocabulary: Set):
        self.vocabulary = vocabulary
        self.word_to_exponent = {k: i for i, k in enumerate(vocabulary)}
        self.exponent_to_word = {i: k for i, k in enumerate(vocabulary)}

    def convert(self, s: Set[str]) -> int:
        return sum(2 ** self.word_to_exponent[k] for k in s)

    def inv_convert(self, n: int) -> Set[str]:
        return {
            self.exponent_to_word[i]
            for i in range(len(self.vocabulary))
            if n & (1 << i)
        }

    @classmethod
    def from_vocabulary(cls, vocabulary: pd.Series) -> "Converter":
        return cls(set([x for xs in vocabulary for x in xs]))


def vectorized_not_null_intersection(df: pd.DataFrame, c1: str, c2: str) -> pd.Series:
    return (df[c1] & df[c2]) != 0


def vectorized_c2_contains_c1(df: pd.DataFrame, c1: str, c2: str) -> pd.Series:
    return df[c2] == (df[c1] & df[c2])
