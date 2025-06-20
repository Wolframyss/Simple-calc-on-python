import math

#Функции для нашеньких операций
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Деление на ноль невозможно!")
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Невозможно извлечь квадратный корень из отрицательного числа!")
    return math.sqrt(x)

#Основаная функция и список возможных действий
def calculator():
    print("What you can do:")
    print("1. Add (+)")
    print("2. Substract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square root (sqrt)")
    print("type 'exit' for closing the programm.")

#бесконечный цикл while true, запрашивающий выбор операции
    while True:
        operation = input("\nВыберите операцию (1-6 или 'выход'): ").strip().lower()

        if operation == 'выход':
            print("Программа завершена.")
            break

        if operation not in ['1', '2', '3', '4', '5', '6']:
            print("Неверная операция! Пожалуйста, выберите 1-6 или 'выход'.")
            continue

        #обработка операций
        try:
            if operation == '6':
                num = float(input("Введите число для извлечения квадратного корня: "))
                result = square_root(num)
                print(f"Результат: √{num} = {result}")
            else:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if operation == '1':
                    result = add(num1, num2)
                    print(f"Результат: {num1} + {num2} = {result}")
                elif operation == '2':
                    result = subtract(num1, num2)
                    print(f"Результат: {num1} - {num2} = {result}")
                elif operation == '3':
                    result = multiply(num1, num2)
                    print(f"Результат: {num1} * {num2} = {result}")
                elif operation == '4':
                    result = divide(num1, num2)
                    print(f"Результат: {num1} / {num2} = {result}")
                elif operation == '5':
                    result = power(num1, num2)
                    print(f"Результат: {num1} ^ {num2} = {result}")

        #обработка ошибок
        except ValueError as e:
            if str(e).startswith("Невозможно"):
                print(f"Ошибка: {e}")
            else:
                print("Ошибка: Пожалуйста, вводите только числа!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    calculator()
