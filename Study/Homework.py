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
#     _speed_page = 3
#     _total_page_count = 0
#
#     def __init__(self, document_name, page_count):
#         self.document_name = document_name
#         Scanner._total_page_count += page_count
#
#         print(f"Dokument: {self.document_name} has {Scanner._total_page_count} page")
#
#     @classmethod
#     def calculate(cls):
#         print("Scanning a document ")
#         total_skan = cls._total_page_count / cls._speed_page
#         minutes = int(total_skan)
#         seconds = int((total_skan - minutes) * 60)
#
#         print(f"Scan completed in {minutes} min {seconds} sec")
#
# scan1 = Scanner("Report", 9)
# scan2 = Scanner("Contract", 6)
#
# Scanner.calculate()

# class Fax(Printer, Scanner):
#
#     def __init__(self):
#         self.printer = Printer()
#         self.scanner = Scanner()
#
#     def fax_print(self, document_name, page_count):
#         print(f"Printing '{document_name}' ({page_count} pages)...")
#         self.printer = Printer(document_name, page_count)
#         print("Document printed successfully!")
#
#     def send_fax(self,document_name, recipient_number):
#         print(f"Sending '{document_name}' to {recipient_number}...")
#         print("Fax sent successfully!")
#
#     def fax_scan(self, document_name, page_count):
#         print(f"Scanning '{document_name}' ({page_count} pages)...")
#         self.scanner = Scanner(document_name, page_count)
#         print("Scan completed!")
#
# fax = Fax()
# fax.fax_print("Report", 5)
# fax.fax_scan("Contract", 10)
# fax.send_fax("Invoice", "+123456789")
