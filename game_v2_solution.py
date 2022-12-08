"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0        # счетчик попыток
    min_number = 1   # определяем минимальное число, левую границу возможного диапазона
    max_number = 101 # определяем максимальное число, правую границу возможного диапазона

    while True:
        count += 1

        # прозводим "двоичный" поиск, сравнивая середину возможного диапазона с исходным числом
        predict_number = min_number + (max_number - min_number) // 2

        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            min_number = predict_number  # "сдвигаем" левую(минимум) границу возможного диапазона, т.к. исходное число больше
        else:
            max_number = predict_number  # иначе "сдвигаем" правую(максимум) границу возможного диапазон, т.к. исходное число меньше (не равно и не больше)
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
