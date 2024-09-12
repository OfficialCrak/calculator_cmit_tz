def add(x: float, y: float) -> float:
    return x+y


def sub(x: float, y: float) -> float:
    return x-y


def multiply(x: float, y: float) -> float:
    return x*y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Ошибка! Деление на ноль")
    return x/y


def change_sign(x: float) -> float:
    return -x


def switch_case(number: int) -> None:
    pass


def main() -> None:
    while True:
        print(
            "\nПростой калькулятор на Python \n"
            "Выберите действие:\n"
            "1 - Сложить два числа\n"
            "2 - Вычесть из первого числа второе\n"
            "3 - Умножить два числа\n"
            "4 - Разделить первое число на второе\n"
            "5 - Изменить знак\n"
            "0 - Выход\n"
        )
        number = int(input("Введите номер действия: "))
        if number == 0:
            print("Выход из программы...")
            break
        switch_case(number)


if __name__ == '__main__':
    main()
