import pytest
from random import randint
from json import loads
from ..vk_test.voight_kampff_test import (
    get_answers,
    get_result,
    check_json_file,
    VoightKampffTest,
)
from ..vk_test.measurements_vital_signs import (
    get_valid_digits,
    get_measurement,
    check_measurements,
)


def test_empty_test():
    assert check_json_file("../empty.json") == False


def test_not_empty_test():
    assert check_json_file("../question.json") == True


@pytest.mark.parametrize(
    ("answer", "result"),
    [
        (
            "1\n12\n60\n1\n2\n1\n12\n60\n1\n2\n1\n12\n60\n1\n2\n1\n12\n60\n1\n2\n1\n12\n60\n1\n2\n1\n12\n60\n1\n2\n1\n12\n60\n1\n2\n1\n12\n60\n1\n2\n1\n12\n60\n1\n2\n1\n12\n60\n1\n2",
            "репликант",
        ),
    ],
)
def test_run_test(monkeypatch, answer, result):
    test = VoightKampffTest("../question.json")
    answer = answer.split("\n")
    it = iter(answer)
    monkeypatch.setattr("builtins.input", lambda _: next(it))
    test.run_test()
    assert test.result == result


@pytest.mark.parametrize(
    ("question", "options", "result"),
    [
        ("Твой любимый цвет?", ["Синий", "Красный", "Фиолетовый", "Зеленый"], "1"),
        (
            "Какой фактульет в Хогвартсе ты выбирешь?",
            ["Гриффиндор", "Когтевра", "Пуффендуй", "Слизерин"],
            "3",
        ),
    ],
)
def test_get_answers(monkeypatch, question, options, result):
    monkeypatch.setattr("builtins.input", lambda _: result)
    assert get_answers(question, options) == int(result)


@pytest.mark.parametrize(
    ("answer", "measurements", "result"),
    [
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0, "репликант"),
        ([4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 50, "человек"),
    ],
)
def test_get_result(answer, measurements, result):
    assert get_result(answer, measurements) == result


@pytest.mark.parametrize(
    ("result"),
    [("1"), ("2")],
)
def test_get_valid_digits(monkeypatch, result):
    monkeypatch.setattr("builtins.input", lambda _: result)
    assert get_valid_digits("Вопрос", 1, 4) == int(result)


@pytest.mark.parametrize(
    ("answer", "result"),
    [
        (["12", "60", "1", "2"], [12, 60, 1, 2]),
        (["16", "100", "6", "8"], [16, 100, 6, 8]),
    ],
)
def test_get_measurement(monkeypatch, answer, result):
    it = iter(answer)
    monkeypatch.setattr("builtins.input", lambda _: next(it))
    assert get_measurement() == result


@pytest.mark.parametrize(
    ("answer", "result"),
    [
        ([[12, 60, 1, 2], [12, 60, 1, 2]], 0),
        ([[16, 100, 6, 8], [16, 100, 6, 8]], 16),
    ],
)
def test_check_measurements(answer, result):
    assert check_measurements(answer) == result
