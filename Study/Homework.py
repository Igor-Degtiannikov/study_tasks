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

###14.03.25###Tasks class

# class Printer:
#     _work_sound = "BEEEEEEEP"
#     _page_count = 0
#     _print_speed = 5
#
#     def __init__(self, print_name, page_count):
#         self.print_name = print_name
#         Printer._page_count += page_count
#
#         print(f"Document added: {self.print_name}, pages: {page_count}")
#
#     @classmethod
#     def calculate_time_work(cls):
#         print(cls._work_sound)
#
#         total_time = cls._page_count / cls._print_speed
#         minutes = int(total_time)
#         seconds = int((total_time - minutes) * 60)
#
#         print(f"Estimated printing time: {minutes} min {seconds} sec")
#         print("FINISH")
#
# doc1 = Printer("report", 8)
# doc2 = Printer("essay", 12)
# Printer.calculate_time_work()

###Спросить Константина, почему я не вижу вывод
# class Phone:
#     def __init__(self, model, battery_level):
#         self.model = model
#         self.battery_level = battery_level
#
#     def make_call(self):
#         if self.battery_level == 0:
#             print("No energy")
#         else:
#             print("Start of call")
#
#     def charge_phone(self, amount):
#         if self.battery_level >= 100:
#             print("The phone is already fully charged.")
#         else:
#             self.battery_level = min(100, self.battery_level + amount)
#             print(f"Charging... New battery level: {self.battery_level}%")
#
#     def __str__(self):
#         return f"Phone model: {self.model}, Battery level: {self.battery_level}%"
#
#
# phone1 = Phone("iPhone 13", 0)
# phone2 = Phone("Samsung S22", 50)
#
# print(phone1)
# print(phone2)
#
# phone1.make_call()
# phone2.make_call()
#
# phone1.charge_phone(30)
# phone2.charge_phone(60)

# class Scanner:
#     _scan_sound = "GGGGGGG"
#     _total_scanned_pages = 0
#     _scan_speed = 2  # страниц в секунду
#
#     def __init__(self, document_name, page_count, color_mode=False):
#         self.document_name = document_name
#         self.page_count = page_count
#         self.color_mode = color_mode  # У каждого объекта свой режим цвета
#
#         print(f"Document added: {self.document_name}, pages: {self.page_count}")
#
#     @classmethod
#     def calculate_scan_time(cls):
#         if cls._total_scanned_pages == 0:
#             print("No documents scanned yet.")
#             return
#
#         scan_speed = cls._scan_speed
#         total_scan = cls._total_scanned_pages / scan_speed
#         minutes = int(total_scan)
#         seconds = int((total_scan - minutes) * 60)
#
#         print(f"Estimated scanning time: {minutes} min {seconds} sec")
#
#     def scan_document(self):
#         print(f"Scanning {self.document_name}...\n{Scanner._scan_sound}")
#
#         scan_speed = Scanner._scan_speed
#         if self.color_mode:
#             scan_speed /= 2
#
#         Scanner._total_scanned_pages += self.page_count
#         print("Scanning complete.")
#
#         Scanner.calculate_scan_time()
#
#     @classmethod
#     def show_total_scanned_pages(cls):
#         print(f"Total scanned pages: {cls._total_scanned_pages}")
#
#
# doc1 = Scanner("Report", 10, color_mode=True)
# doc2 = Scanner("Essay", 5)
#
# doc1.scan_document()
# doc2.scan_document()
#
# Scanner.show_total_scanned_pages()