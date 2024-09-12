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
