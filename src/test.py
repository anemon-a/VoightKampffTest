class Voight_Kampff_Test:
    def __init__(self, questions: dict[str, dict]) -> None:
        self.questions = questions
        self.answers = list()
        self.measurements = list()

    def perform_test(self) -> None:
        for i in self.questions.keys():
            self.answers.append(ask_questions(i, self.questions[i]))
            self.measurements.append(measure_vital_signs())


def ask_questions(question_number: int, question_content: dict[str, list]) -> int:
    for question, answers in question_content.items():
        print(str(question_number) + ". " + question)
        for i in range(len(answers)):
            print(str(i + 1) + ") " + answers[i])

    while True:
        result = input("Введите вариант ответа цифрой (1-4): ")
        if result.isdigit() and 1 <= int(result) <= 4:
            return result
        else:
            print("Пожалуйста, введите цифру от 1 до 4.")


def measure_vital_signs():
    vital_signs = {
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
            result = input(vital_signs[i][0])
            if (
                result.isdigit()
                and vital_signs[i][1] <= int(result) <= vital_signs[i][2]
            ):
                measurements.append(result)
                break
            else:
                print(
                    f"Пожалуйста, введите цифру от {vital_signs[i][1]} до {vital_signs[i][2]}."
                )

    return measurements
