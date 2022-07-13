from fast_filters.binary import Converter


def test_converter():
    vocabulary = ["a", "b", "c"]
    converter = Converter(vocabulary=vocabulary)

    x = ["a"]
    assert converter.inv_convert(converter.convert(x)) == x
    x = ["a", "b"]
    assert converter.inv_convert(converter.convert(x)) == x


def test_inv_converter():
    vocabulary = ["a", "b", "c"]
    converter = Converter(vocabulary=vocabulary)

    for i in range(7):
        assert converter.convert(converter.inv_convert(i)) == i
