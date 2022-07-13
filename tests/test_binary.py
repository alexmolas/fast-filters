import pandas as pd

from fast_filters.binary import Converter, vectorized_not_null_intersection


def test_converter():
    vocabulary = {"a", "b", "c"}
    converter = Converter(vocabulary=vocabulary)

    x = {"a"}
    assert converter.inv_convert(converter.convert(x)) == x
    x = {"a", "b"}
    assert converter.inv_convert(converter.convert(x)) == x


def test_converter_empty_set():
    vocabulary = {"a", "b", "c"}
    converter = Converter(vocabulary=vocabulary)

    x = set()
    assert converter.convert(x) == 0


def test_inv_converter():
    vocabulary = {"a", "b", "c"}
    converter = Converter(vocabulary=vocabulary)

    for i in range(7):
        assert converter.convert(converter.inv_convert(i)) == i


def test_converter_from_vocabulary():
    vocabulary = pd.Series(["a", "b", "c"])
    converter = Converter.from_vocabulary(vocabulary)

    x = {"a"}
    assert converter.inv_convert(converter.convert(x)) == x
    x = {"a", "b"}
    assert converter.inv_convert(converter.convert(x)) == x


def test_vectorized_not_null_intersection():
    df = pd.DataFrame({"a": [[1, 2, 3], [4, 5, 6]], "b": [[1], [4]]})
    vocabulary = {1, 2, 3, 4, 5, 6}
    converter = Converter(vocabulary=vocabulary)
    df["a_encoded"] = df["a"].map(converter.convert)
    df["b_encoded"] = df["b"].map(converter.convert)
    assert all(
        vectorized_not_null_intersection(df, "a_encoded", "b_encoded")
        == pd.Series([True, True])
    )
