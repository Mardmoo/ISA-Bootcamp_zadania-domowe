import pytest
from trojkat import trojkat


def test_trojkat_input():
    input_a = 'a'
    input_b = 'b'
    with pytest.raises(TypeError):
        trojkat(input_a, input_b)


def test_trojkat_values():
    input_a = 2
    input_b = 3
    expected = 5
    result = trojkat(input_a, input_b)
    assert result == expected


def test_trojkat_values_second():
    input_a = 6
    input_b = 8
    expected = 10
    result = trojkat(input_a, input_b)
    assert result == expected
