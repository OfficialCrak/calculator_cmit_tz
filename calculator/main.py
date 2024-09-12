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
    if number == 1:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print(f"Результат {num1} + {num2} = {add(num1, num2)}")
    elif number == 2:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print(f"Результат {num1} - {num2} = {sub(num1, num2)}")
    elif number == 3:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print(f"Результат {num1} * {num2} = {multiply(num1, num2)}")
    elif number == 4:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        try:
            print(f"Результат {num1} / {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    elif number == 5:
        num = float(input("Введите число: "))
        print(f"Результат -1 * {num} = {change_sign(num)}")
    else:
        print("Некорректный выбор. Попробуйте снова.")


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
