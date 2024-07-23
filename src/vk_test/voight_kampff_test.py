import json
from os import path
from .measurements_vital_signs import (
    get_measurement,
    check_measurements,
    get_valid_digits,
)


class VoightKampffTest:
    """VoightKampffTes class, contaioning two method: run_test"""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.questions = dict()
        self.answers = list()
        self.measurements = list()
        self.result = ""

    def run_test(self) -> None:
        """Runs the test and outputs the resulting answer"""
        if check_json_file(self.filename):
            with open(self.filename) as f:
                self.questions = json.load(f)
            for question, options in self.questions.items():
                self.answers.append(get_answers(question, options))
                self.measurements.append(get_measurement())
            self.result = get_result(
                self.answers, check_measurements(self.measurements)
            )
            print("Результат:\nТы - " + self.result)
        else:
            print("File can't be opened")


def get_answers(question: str, options: list[str]) -> int:
    """Counts the points for answering the test questions, returning the total"""
    print(question)
    for i in range(len(options)):
        print(str(i + 1) + ") " + options[i])
    answer = get_valid_digits("Введите вариант ответа цифрой (1-4): ", 1, 4)
    return answer


def get_result(answers: list[int], measurements: int) -> str:
    """Returns the test result"""
    result = sum(answers) + measurements
    print(answers, measurements)
    if result > 60:
        return "человек"
    else:
        return "репликант"


def check_json_file(filename: str) -> bool:
    """Checks if the file path is valid"""
    if (
        path.isfile(filename)
        and path.splitext(filename)[1] == ".json"
        and path.getsize(filename) != 0
    ):
        return True
    return False
