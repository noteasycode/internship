import string
from random import randrange, choice, sample, randint
from datetime import datetime, timedelta


def by_value(item):
    """Function from the previous task."""
    return item[1]


def selection_sort(nums):
    """Function from the previous task."""
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


#   Creating global variable
int_variable = 4


def my_func():
    """Put the task from previous lesson in this function"""
    global int_variable
    str_variable = "47"

    print("Сравнение типа переменных:")
    print(type(str_variable) != type(int_variable), end='\n\n')

    print("Конвертация числовой переменной в строчную:")
    int_variable = str(int_variable)
    print(type(int_variable), end='\n\n')

    list_variable = ['django', 'flask', 'pandas', 'numpy', 'selenium']
    print("Добавляем элемент в конец списка:")
    list_variable.append('tensorflow')
    print(list_variable, end='\n\n')

    print("Добавляем элемент в нужную позицию в списке:")
    list_variable.insert(3, 'matplotlib')
    print(list_variable, end='\n\n')

    print("Удаляем первый элемент:")
    list_variable.remove('django')
    print(list_variable, end='\n\n')

    print("Удаляем элемент списка по индексу:")
    list_variable.pop(0)
    print(list_variable, end='\n\n')

    print("Разворачиваем список:")
    list_variable.reverse()
    print(list_variable, end='\n\n')

    print("Подсчитуем количество элементов pandas в списке:")
    print(list_variable.count('pandas'), end='\n\n')

    print("Создаём копию списка:")
    list_variable2 = list_variable.copy()
    print(list_variable2, end='\n\n')

    print("Сортируем первый список используя алгоритм сортировки выбором:")
    selection_sort(list_variable)
    print(list_variable, end='\n\n')

    print("Сортируем второй список стандартным методом:")
    list_variable2.sort()
    print(list_variable2, end='\n\n')

    print("Сортируем строку по алфавиту:")
    print(sorted("This is a test string for Internship Onix for python".split(),
                 key=str.lower
                 ), end='\n\n'
          )

    print("Создаём словарь:")
    cookies_recipe = {
        "butter": "460 g",
        "brown sugar": "440 g",
        "granulated sugar": "400 g",
        "eggs": "4",
        "vanilla extract": "1 tablespoon",
        "flour": "650 g",
        "baking powder": "2 teaspoons"
    }
    print(cookies_recipe, end='\n\n')

    print("Добавляем элемент в словарь:")
    cookies_recipe["chocolate chips"] = "700 g"
    print(cookies_recipe, end='\n\n')

    print("Получаем значение из словаря по ключу:")
    print(cookies_recipe["baking powder"], end='\n\n')

    print("Удаляем элемент из словаря:")
    del cookies_recipe["chocolate chips"]
    print(cookies_recipe, end='\n\n')

    print("Получаем все ключи словаря:")
    print(cookies_recipe.keys(), end='\n\n')

    print("Получаем все значения словаря:")
    print(cookies_recipe.values(), end='\n\n')

    print("Сортируем словарь по ключам:")
    for key in sorted(cookies_recipe):
        print(key, "->", cookies_recipe[key])

    print()
    print("Сортируем словарь по значениям:")
    for key, value in sorted(cookies_recipe.items(),
                             key=by_value):
        print(key, "->", value)


def multiply_global_num(num):
    global int_variable
    new_list = []
    new_list.append(int(int_variable) * int(num))
    return new_list, len(new_list)


def args_kwargs(*args, **kwargs):
    print(args)
    for key, value in kwargs.items():
        print(key, "->", value)


def is_divisible_by(num, divisor):
    if (num % divisor) == 0:
        print(f"The number {num} is divisible by number {divisor} without remainder.")
    else:
        print(f"The number {num} is not divisible by number {divisor} without remainder.")


def fibonacci(num):
    if num < 2:
        return num
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))


if __name__ == "__main__":
    my_func()
    print(multiply_global_num(4))
    args_kwargs(1, 2, my_name="Denis", my_country='Ukraine')
    is_divisible_by(12, 4)
    print(fibonacci(13))

    print("\nTask 5")
    now = datetime.today()
    tomorrow = now + timedelta(days=1)
    str_date = datetime.strptime("2020-02-03 09:18:36.000", "%Y-%m-%d %X.%f")
    print(f"Today: {now.strftime('%d-%m-%Y %H:%M')}\nTomorrow: {tomorrow.strftime('%d-%m-%Y %H:%M')}\n"
          f"Converted string to datetime: {str_date}\n"
          f"Day: {str_date.strftime('%d')}\nMonth: {str_date.strftime('%m')}\n"
          f"Year: {str_date.strftime('%Y')}\nHour: {str_date.strftime('%H')}\n"
          f"Seconds: {str_date.strftime('%S')}")

    num = [randrange(100, 999, 5) for _ in range(3)]
    print(f"The numbers {', '.join(str(x) for x in num)} are divisible by 5")
    print(f"Random symbols: {''.join(choice(string.ascii_letters + string.digits) for i in range(10))}")
    tickets = [randrange(1000000000, 10000000000) for _ in range(100)]
    print(f"The lottery ticket that won are: {', '.join(str(x) for x in sample(tickets, 2))}")
    try:
        x = 1 / 0
    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished")