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


def get_measurement() -> list[int]:
    output = {
        0: ["Введите дыхание от 12 до 16 вдохов в минуту: ", 12, 16],
        1: [
            "Введите частоту сердечных сокращений от 60 до 100 ударов в минуту: ",
            60,
            100,
        ],
        2: ["Введите уровень покраснения от 1 до 6: ", 1, 6],
        3: ["Введите расширение зрачков от 3 до 8 мм: ", 2, 8],
    }
    measurements = list()
    for i in range(0, 4):
        while True:
            result = input(output[i][0])
            if result.isdigit() and output[i][1] <= int(result) <= output[i][2]:
                measurements.append(result)
                break
            else:
                print(f"Пожалуйста, введите цифру от {output[i][1]} до {output[i][2]}.")

    return measurements


def get_result(answers: list[int], measurements: int) -> None:
    result = sum(answers) + measurements
    if result >= 50:
        print("Ты - репликант")
    else:
        print("Ты - человек")


def check_measurements(measurements: list[list[int]]) -> int:
    limits = [(12, 16), (60, 100), (1, 6), (2, 8)]
    result = 0
    for m in measurements:
        for i in range(0, 4):
            if int(m[i]) < limits[i][0] + limits[i][1] / 2:
                result += 2
    return result
