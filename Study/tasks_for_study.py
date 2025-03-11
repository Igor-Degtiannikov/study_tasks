##task for repeat methods for string
#
# mes = input("Enter your message: ").strip().lower()
#
# mes_digit = mes.isdigit()
#
# clean_mes = mes.translate(str.maketrans("","","!?,."))
# mes_alph = clean_mes.replace(" ", "").isalpha()
#
# if mes_digit:
#     print("Wrong! Your text has numbers")
# else:
#     mes_len_alph = len(mes)
#
# replase_map = str.maketrans({"!": "."})
# mes_replased = mes.translate(replase_map)
#
# mes_spl = mes.split()
# mes_all = "\n".join([str(mes), str(mes_digit), str(mes_alph), str(mes_len_alph), str(mes_replased), str(mes_spl)])
# print(mes_all)

##task for repeat Functions
### Разобрать с Константином!
# def get_numbers():
#     user_input = input()
#     return list(map(int, user_input.split()))
#
# def amount(num):
#     total = 0
#     for i in num:
#         total += i
#     print("Amount numbers: ", total)
#
# def find_max(num):
#     max_number = max(num)
#     print("Max numbers: ", max_number)
#
# def multiplication(num):
#     total = 1
#     for i in num:
#         total *= i
#     print("multiplication: ", total)
#
# num_list = get_numbers()
#
# amount(num_list)
# find_max(num_list)
# multiplication(num_list)

###@classmethod
# class Dog:
#     __bark_sound = "B00000RK!"
#     __count = 0
#
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         Dog.__count += 1
#
#     @classmethod
#     def get_total_count(cls):
#         return cls.__count
#
#     @classmethod
#     def bark(cls):
#         print(cls.__bark_sound)
#
#     @classmethod
#     def create_from_string(cls, dog_string):
#         name, breed = dog_string.split(":")
#         return cls(name, breed)
#
#@staticmethod
# def calculate_age_in_dog_years(age):
#     dog_years = age * 7
#     return dog_years

# dog_string = "Buddy:Golden Retriever"
# buddy = Dog.create_from_string(dog_string)
# print(buddy.name)



