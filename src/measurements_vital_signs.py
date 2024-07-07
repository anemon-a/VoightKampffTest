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


def get_measurement() -> list[int]:
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


def check_measurements(measurements: list[list[int]]) -> int:
    result = 0
    for m in measurements:
        for i in range(0, 4):
            if int(m[i]) < output[i][0] + output[i][1] / 2:
                result += 2
    return result
