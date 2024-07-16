message = {
    0: ["Введите дыхание от 12 до 16 вдохов в минуту: ", 12, 16],
    1: [
        "Введите частоту сердечных сокращений от 60 до 100 ударов в минуту: ",
        60,
        100,
    ],
    2: ["Введите уровень покраснения от 1 до 6: ", 1, 6],
    3: ["Введите расширение зрачков от 2 до 8 мм: ", 2, 8],
}


def get_valid_digits(message: str, min_value: int, max_value: int) -> int:
    """Checks the input from the user for validity"""
    while True:
        answer = input(message)
        if answer.isdigit() and min_value <= int(answer) <= max_value:
            return int(answer)
        else:
            print(f"Пожалуйста, введите цифру от {min_value} до {max_value}.")


def get_measurement() -> list[int]:
    """Adds measurements of vital signs of a person, such as breathing, heart rate, degree of redness, pupil dilation"""
    measurements = list()
    for i in range(0, 4):
        measurements.append(
            get_valid_digits(message[i][0], message[i][1], message[i][2])
        )
    return measurements


def check_measurements(measurements: list[list[int]]) -> int:
    """Respiratory indicators, heart rate, degree of redness, pupil dilation are checked and a rare score is calculated"""
    result = 0
    for m in measurements:
        for i in range(0, 4):
            if m[i] > (message[i][1] + message[i][2]) / 2:
                result += 2
    return result
