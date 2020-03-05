int_variable = 47
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
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

selection_sort(list_variable)
print(list_variable, end='\n\n')

print("Сортируем второй список стандартным методом:")
list_variable2.sort()
print(list_variable2, end='\n\n')

print("Сортируем строку по алфавиту:")
print(sorted("This is a test string for Internship Onix for python".split(),
             key=str.lower), end='\n\n')

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

def by_value(item):
    return item[1]
for key, value in sorted(cookies_recipe.items(),
                   key=by_value):
    print(key, "->", value)
