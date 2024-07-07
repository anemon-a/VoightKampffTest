from measurements_vital_signs import get_measurement, check_measurements


class Voight_Kampff_Test:
    def __init__(self, questions: dict[str, dict]) -> None:
        self.questions = questions
        self.answers = list()
        self.measurements = list()

    def perform_test(self) -> None:
        for i in self.questions.keys():
            self.answers.append(get_answers(i, self.questions[i]))
            self.measurements.append(get_measurement())
        get_result(self.answers, check_measurements(self.measurements))


def get_answers(question_number: int, question_content: dict[str, list]) -> int:
    for question, options in question_content.items():
        print(str(question_number) + ". " + question)
        for i in range(len(options)):
            print(str(i + 1) + ") " + options[i])

    while True:
        answer = input("Введите вариант ответа цифрой (1-4): ")
        if answer.isdigit() and 1 <= int(answer) <= 4:
            return int(answer)
        else:
            print("Пожалуйста, введите цифру от 1 до 4.")


def get_result(answers: list[int], measurements: int) -> None:
    result = sum(answers) + measurements
    if result >= 50:
        print("Ты - репликант")
    else:
        print("Ты - человек")
