int_variable = 47
str_variable = "47"

#   Сравнение типа переменных.
print(type(str_variable) != type(int_variable))

#   Конвертация числовой переменной в строчную.
int_variable = str(int_variable)
print(type(int_variable))

List_variable = ['django', 'flask', 'pandas', 'numpy', 'selenium']
#   Добавляем элемент в конец списка
List_variable.append('tensorflow')
print(List_variable)

#   Добавляем элемент в нужную позицию в списке
List_variable.insert(3, 'matplotlib')
print(List_variable)

#   Удаляем первый элемент
List_variable.remove('django')
print(List_variable)

#   Удаляем элемент списка по индексу
List_variable.pop(0)
print(List_variable)

#   Разворачиваем список
List_variable.reverse()
print(List_variable)

#   Подсчитуем количество элементов в списке
print(List_variable.count('pandas'))

#   Создаём копию списка
List_variable2 = List_variable.copy()
print(List_variable2)

#   Сортируем первый список используя алгоритм сортировки выбором
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

selection_sort(List_variable)
print(List_variable)

#  Сортируем второй список стандартным методом
List_variable2.sort()
print(List_variable2)

#   Сортируем строку по алфавиту
print(sorted("This is a test string for Internship Onix for python".split(),
             key=str.lower))

#   Создаём словарь
cookies_recipe = {
    "butter": "460 g",
    "brown sugar": "440 g",
    "granulated sugar": "400 g",
    "eggs": "4",
    "vanilla extract": "1 tablespoon",
    "flour": "650 g",
    "baking powder": "2 teaspoons"
}
print(cookies_recipe)

#   Добавляем элемент в словарь
cookies_recipe["chocolate chips"] = "700 g"
print(cookies_recipe)