import pytest
from ..vk_test.voight_kampff_test import get_answers
from ..vk_test.measurements_vital_signs import get_valid_answers


@pytest.mark.parametrize(
    ("question", "options", "result"),
    [
        ("?", ["a", "b", "c", "d"], "2"),
        ("?", ["a", "b", "c", "d"], "3"),
        ("?", ["a", "b", "c", "d"], "4"),
    ],
)
def test_get_valid_answers(monkeypatch, question, options, result):
    s = ["2", "3", "4", "1"]
    monkeypatch.setattr("builtins.input", lambda _: result)
    assert get_answers(question, options) == int(result)


def test_get_valid_digit(monkeypatch):
    s = "2"
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert get_valid_answers("?", 1, 4) == 2
