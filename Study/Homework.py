### introspection
## Узнавать тип данных (type())
# print(type("Hello"))     # <class 'str'>

## Узнавать уникальный идентификатор объекта в памяти(id())
# print(id(a), id(b))  # У них могут быть одинаковые id из-за интернирования строк
# print(id(c), id(d))  # Здесь id разные, так как списки создаются в новой области памяти

## Проверять методы объекта (dir())
# print(dir(text))  # Покажет все методы, доступные для строк

## Читать документацию (help())
# print(help(str))         # Общая справка по строкам
# print(help(str.upper))

## Проверяет, можно ли вызвать объект, как функцию (callable())
# print(callable(len))      # True (функция)
# print(callable("hello"))  # False (строка не вызываема)

## Проверяет, принадлежит ли объект к определённому классу isinstance()
# print(isinstance("hello", str))   # True
# print(isinstance(42, str))        # False

## Проверяет, является ли класс наследником другого класса issubclass()
# class Animal: pass
# class Dog(Animal): pass
#
# print(issubclass(Dog, Animal))  # True
# print(issubclass(Animal, Dog))  # False

## Возвращает словарь атрибутов объекта (если объект поддерживает это) vars()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p = Person("Alice", 30)
# print(vars(p))  # {'name': 'Alice', 'age': 30}

## Показывают глобальные и локальные переменные globals() and locals()
# a = 10
# b = 20

# def my_func():
#     x = 5
#     print(locals())  # {'x': 5} — только локальные переменные внутри функции
#
# print(globals())  # Покажет все глобальные переменные в программе

###string methods

## print("Hello, World!!".strip("!")) - удаляет все ! в начале и конце строки.
# print("Hello, World!!".removesuffix("!")) - удаляет только один !

## replace_map = str.maketrans({ - str.maketrans({...}) создаёт таблицу замены символов.
#     "!": "",
#     ",": "",
# })
#
# print("Hello, World!!".translate(replace_map)) -translate(replace_map) применяет эту таблицу к строке, удаляя ! и ,

## text = "Hello world"
# words = text.split()
#
# print(f"{words[0]}\n{words[1]}") - раздел по индексу
# print("\n".join(text.split())) - заменяет пробелы на перенос строки \n
# print(text.replace(" ", "\n")) - делает то же самое.

## text = "qwertyuiop"
# result = ""
#
# result = [letter.upper() if letter in "eouai" else letter for letter in text]
# print("".join(result))
