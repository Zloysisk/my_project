number = int(input(f"До скольки выводить ?: "))
for quter in range(1, number // 2 + 1):
 quter *= 2
 print(f"{quter} в степени 3 = {quter ** 3}")

# +++++++++++++++++++++++++++++++++++++++++++++++

hour = int(input('Укажите кол-во времени длительности эксперемента: '))
print()
num_animal = 1
for animal in range(1, hour // 3 + 1):
 num_animal *= 2
 print(f"Прошло часов:  {animal * 3}.")
 print(f"Клеток:  {num_animal}.")
 print(f"Часов до конца эксперемента:  {hour - animal * 3}.")
 print()
print("Наблюдение завершено")

# +++++++++++++++++++++++++++++++++++++++++++++++

numb = int(input('Укажите число: '))
for qube in range(1, numb // 2 + numb % 2 + 1):
 qube_2 = qube * 2 - 1
 print(f"{qube_2} в квадрате равен {qube_2 ** 2}")

# +++++++++++++++++++++++++++++++++++++++++++++++

number = int(input('Укажите число: '))
for xyi in range(1, number + 1, 2):
 print(f"{xyi} в кубе равен {xyi ** 3}")

# +++++++++++++++++++++++++++++++++++++++++++++++
chair = int(input('Введите номер стула: '))
xuy = 0
for number in range(1, chair + 1, 5):
 print(f"Номер стула: {number}")
 xuy += number
print(f"Сумма: {xuy}")

# ++++++++++++++++++++++++++++++++++++++++++++++++

wake_up = int(input('Время подъёма: '))
hour = 0
water = 0
eat_all = 0
for begin in range(wake_up, 23 + 1, 3):
 water += 1
 print(f"вермя: {begin}")
 eat = int(input('Сколько колорий съел ?: '))
 eat_all += eat
print(f"Воды выпито: {water}, калорий съедено:{eat_all}")

# ++++++++++++++++++++++++++++++++++++++++++++++++

time = int(input('Сколько секунд отсчитывать ? '))
for search in range(time, -1, -1):
 print(search)
print('Я иду искать !')

# ++++++++++++++++++++++++++++++++++++++++++++++++

soldier = int(input('Сколько солдат в строю: '))
ask = int(input('Cколько правил прописано в воинском уставе: '))
push_up = 0
for qustion in range(soldier - 4, 1, -4):
 answer = int(input('Ответ: '))
 if answer != ask:
  print(f"Неправильно {qustion * 10} отжиманий")
  push_up += qustion * 10
print(f"Количество отжиманий {push_up}")

# +++++++++++++++++++++++++++++++++++++++++++++++++

timer = int(input('До скольки считать? '))
for search in range(timer, -1, -2):
 print(search)
print('Я иду искать')

# +++++++++++++++++++++++++++++++++++++++++++++++++

bad = 0
students = 0
for students in range(5):
 question = input('“Кто написал произведение?” ')
 if question == 'Пушкин' or question == 'пушкин':
  print('Правильно, садись')
  break
 print('Садись 2')
 bad += 1
print()
print(f"Количество двоечников в классе: {bad}")

# +++++++++++++++++++++++++++++++++++++++++++++++++

while True:
 ask = input('Ты выполнил работу ? ')
 if ask == 'Да, конечно, сделал':
  break
print('Возьми с полки пирожок')

# +++++++++++++++++++++++++++++++++++++++++++++++++

name = input('Как тебя зовут ? ')
answer = input(f"{name}, купи слона ")
joke = input(f"Все говорят “{answer}”, а ты купи слона! ")
number = 2
while True:
 if joke == 'Заебал':
  print(f"Вы не купили слона {number} раз(а)")
  break
 joke = input(f"Все говорят “{joke}”, а ты купи слона! ")
 number += 1

# +++++++++++++++++++++++++++++++++++++++++++++++++

word = input('Введите текст: ')
big = 'Ы'
small = 'ы'
s_word = 0
b_word = 0

for revision in word:
 if revision == small:
  s_word += 1
 if revision == big:
  b_word += 1

print()
print(f"Больших букв Ы: {b_word}")
print()
print(f"Маленьких букв ы: {s_word}")

# +++++++++++++++++++++++++++++++++++++++++++++++++

print("----------", end="\n|00000000|" * 4)
print("\n----------")

# or

print("-" * 10)
for _ in range(4):
 for i in range(10):
  if i == 0 or i == 9:
   print("|", end="")
  else:
   print("0", end="")
 print()
print("-" * 10)

# +++++++++++++++++++++++++++++++++++++++++++++++++

num = int(input('Укажите первое число IP адреса: '))
step = int(input('Укажите шаг: '))
summ = 0

print("\nIp adress:", end=' ')
for count in range(3):
 print(num, end='.')
 summ += num
 num += step
print(summ)

# +++++++++++++++++++++++++++++++++++++++++++++++++

number = int(input("Введите количество голов: "))
print('-=- ', end="")
for goal in range(0, number * 10 + 1, 10):
 print(goal, '-=- ', end="")

# +++++++++++++++++++++++++++++++++++++++++++++++++

mat = ["xyi", "pizda", "zalupa"]
h, p, z = mat
print(f"-=- {p} -=- {p} -=- {p} -=-")
print(f"+=+" * 12)
print(f"-=- {z} -=- {z} -=- {z} -=-")
print(f"+=+" * 12)
print(f"-=- {h} -=- {h} -=- {h} -=-")

# +++++++++++++++++++++++++++++++++++++++++++++++++

for row in range(1, 10):
 for col in range(1, 10):
  print(f"\t{row * col}", end=" ")
 print()

# +++++++++++++++++++++++++++++++++++++++++++++++++

n = int(input('Укажите число "N": '))
for row in range(0, n + 1):
 for col in range(0, n + 1):
  print(f"\t{row + col}", end=" ")
 print()

# +++++++++++++++++++++++++++++++++++++++++++++++++

for row in range(0, 10):
 for col in range(0, -10, -1):
  print(f"\t{row + col}", end=" ")
 print()

# +++++++++++++++++++++++++++++++++++++++++++++++++

numb = int(input('Введите размер матрицы: '))
for row in range(1, numb + 1):
 for col in range(1, numb + 1):
  if row % 2 != 0:
   print(f"\t{col}", end="")
  else:
   print(f"\t{row}", end="")
 print()

# +++++++++++++++++++++++++++++++++++++++++++++++++

size = int(input('Размер матрицы: '))
for row in range(1, size + 1):  # строка
 for col in range(1, size + 1):  # столбец
  if col % 3 == 0:

   print(f"\t{col}", end=" ")
  else:

   print(f"\t{row}", end=" ")
 print()

# +++++++++++++++++++++++++++++++++++++++++++++++++

for row in range(20):
 for col in range(50):
  if col == 24:
   print('|', end='')
  elif row == 9:
   print('-', end='')

  else:
   print(' ', end='')
 print()

# +++++++++++++++++++++++++++++++++++++++++++++++++

for row in range(20):  # строк
 for col in range(30):  # столбцов
  if row == 0:
   print(f"-", end="")
  elif col == 5 or col == 24 - 1:
   print(f"||", end='')
  else:
   print(' ', end='')
 print()

# +++++++++++++++++++++++++++++++++++++++++++++++++

for row in range(20):
 for col in range(50):
  if col == 24:
   print('|', end='')
  elif col == row + 29:
   print('\\', end='')
  elif col == -row + 19:
   print('/', end='')
  elif row == 9:
   print('-', end='')
  else:
   print(' ', end='')
 print()

# +++++++++++++++++++++++++++++++++++++++++++++++++

seqnum = int(input("Сколько будет чисел?: "))
numeral = int(input("Как цифру считать?: "))
while numeral < 0 or numeral > 9:
 numeral = int(input(f"Цифра должна быть в диапозоне от 0 до 9, введите новыю цифру: "))
numeralCount = 0
for num in range(seqnum):
 number = int(input(f"Введите {num}-е число: "))
 while number > 0:
  if number % 10 == numeral:
   numeralCount += 1
  number //= 10
print(f"Цифр {numeral} в последовательности: {numeralCount}")

# +++++++++++++++++++++++++++++++++++++++++++++++++

people = int(input('Укажите количество людей: '))
for hour in range(people + 1):
 print(f"Идёт час: {hour}")
 for num in range(hour, people):
  print(f"Людей осталось в очереди: {num}")
 print()
print("Очередь коничилась")

# +++++++++++++++++++++++++++++++++++++++++++++++++

size = int(input("Введите число: "))

for row in range(size + 1):  # строка
 for col in range(row, size + 1):  # столбец
  print(f"\t{col}", end="")
 print()

# +++++++++++++++++++++++++++++++++++++++++++++++++

number = float(input("Сумма ставки: "))
percent = float(input("\nКоэффициент: "))

win = round(number * percent, 2)
print("\nВыйгрыш:", win)

# +++++++++++++++++++++++++++++++++++++++++++++++++

years = int(input("Укажите возвраст: "))
tempreche = float(input("Укажите температуру тела: "))

present = round(years * tempreche * 1.5, 2)
print(f"\nПодарок на день рождение {present} рублей")

# +++++++++++++++++++++++++++++++++++++++++++++++++

height = float(input('Укажите рост: '))
weight = float(input('\nУкажите вес: '))

index = round(weight / height ** 2, 2)
if index < 18.5:
 print(f"\nДистрофан {index}")
elif index < 25 or index < 30:
 print(f"\nНормас {index}")
else:
 print(f"\nЖиробас {index}")

# +++++++++++++++++++++++++++++++++++++++++++++++++

chatle = int(input("Сколько чатлов? "))
ship = int(chatle / 1100)

cr = float(chatle / 2200)

print(f"\nЭто {cr} CR")
print(f"\nМожно купить {ship} кораблей")

# +++++++++++++++++++++++++++++++++++++++++++++++++

print("Введите местоположение фигуры")
x = float(input("\nПо горизонтали: "))
y = float(input("\nПо вертикали: "))

xsqure = int(x * 10)
ysqure = int(y * 10)

if xsqure < 0.8 or ysqure < 0.8:
 print("\nКлетки с такой координатой не существует")

else:
 print(f"\nФигура находится в клетке ({xsqure}, {ysqure})")

{y_number}")
center_x = x_number / 10 + 0.05
center_y = y_number / 10 + 0.05
delta_x = round(center_x - x_coord, 3)
delta_y = round(center_y - y_coord, 3)
print(f"Поправьте положение фигуры на ({delta_x}, {delta_y})")

# +++++++++++++++++++++++++++++++++++++++++++++++++

import math

a = int(input('Введите длину стороны "A": '))
b = int(input('Введите длину стороны "B": '))
c = int(input('Введите длину стороны "C": '))

p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"\nПлощадь 'S' ровна {s}")

# +++++++++++++++++++++++++++++++++++++++++++++++++

import math

range = int(input("Укажите расстояние до цели: "))
direction = int(input("Укажите направление в градусах: "))

direction /= 57.2958
x = math.cos(direction) * range
y = math.sin(direction) * range

print(f"Координаты вражеского танка {x},{y}")

# +++++++++++++++++++++++++++++++++++++++++++++++++

import math

number = float(input('Введите натуральное число: '))

number_low = math.floor(number)
print(f"\nОкругление в низ: {number_low}")
number_hight = math.ceil(number)
print(f"\nОкругление в верх: {number_hight}")
modul_number = abs(number)
print(f"\nМодуль числа: {modul_number}")
sqrt_number = math.sqrt(modul_number)
print(f"\nМодуль числа: {sqrt_number}")
exp_number = math.exp(number)
print(f"\nЭкспонента: {exp_number}")

sin_number = math.sin(number)
print(f"\nСинус числа: {sin_number}")
cos_number = math.cos(number)
print(f"\nКосинус числа: {cos_number}")
while number < 0:
 number = int(input('\nПовторите ввод для расчета: '))
log_2_number = math.log2(number)
print(f"\nНатуральный логарифм числа: {log_2_number}")
log_10_number = math.log10(number)
print(f"\nЛогарифм числа по основанию 2: {log_10_number}")
log_number = math.log(number, 2)
print(f"\nНатуральный логарифм числа: {log_number}")
factorial_number = math.factorial(number)
print(f"\nФакториал числа: {factorial_number}")


# +++++++++++++++++++++++++++++++++++++++++++++++++

def greeting():
 print('\nПривет!')
 print('Добро пожаловать!')


while True:
 a = input('\nЗайдёте? Да/Нет: ')
 if a == 'Да':
  greeting()
 print('\nСледующий.')


# +++++++++++++++++++++++++++++++++++++++++++++++++

def prod_n_prod():
 a = int(input("\n Укажите кол-во в шт.: "))
 b = int(input("\n Укажите кол-во в шт.: "))
 print(f"\nВсего, {a + b}, шт.")


print("\nСколько мешков рыбы и мяса?")

prod_n_prod()

print("\nСколько буханок белого и чёрного хлеба?")

prod_n_prod()

print("\nСколько вёдер воды и молока?")

prod_n_prod()


# +++++++++++++++++++++++++++++++++++++++++++++++++

def fio():
 print("Фамилия: Иванов")
 print("Имя: Василий")
 print("Улица: Пушкина")
 print("Дом: 32")
 print()


fio()
fio()
fio()


# +++++++++++++++++++++++++++++++++++++++++++++++++

def aboutWater(price):
 print("Название: КлирВотер")
 print("Производитель: ВодЗавод")
 print(f"Цена {price}")
 print()
 print()


aboutWater(25)
aboutWater(30)
aboutWater(40)

# +++++++++++++++++++++++++++++++++++++++++++++++++

import math


def sphereArea(r):
 print(f"\nS = {4 * math.pi * math.pow(r, 2)}")


def sphereVolume(r):
 print(f"\nV = {4 / 3 * math.pi * math.pow(r, 3)}")


r = int(input("Укажите радиус планеты: "))
sphereArea(r)
sphereVolume(r)


# +++++++++++++++++++++++++++++++++++++++++++++++++

def is_prime(number):
 for i in range(2, int(number ** .5) + 1):
  if number % i == 0:
   return False
 return True


n = int(input("Введите количество чисел в последовательности: "))
count = 0
for i in range(n):
 new_number = int(input("Введите число: "))
 if is_prime(new_number):
  count += 1

print(count)


# +++++++++++++++++++++++++++++++++++++++++++++++++

def middle():
 if a > b:
  print("A не может быть больше В")
 else:
  print((a + b) / 2)


a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
middle()


# +++++++++++++++++++++++++++++++++++++++++++++++++

def adress(surname, name, country, city, street, num_home, num_flat):
 print(f"Фамилия: {surname}")
 print(f"Имя: {name}")
 print(f"Страна проживания: {country}")
 print(f"Город: {city}")
 print(f"Улица: {street}")
 print(f"Номер дома: {num_home}")
 print(f"Номер квартиры: {num_flat}")
 print()


adress("Иванов", "Иван", "Россия", "Москва", "Островетянова", 19, 23)
adress("Сергеев", "Константин", "Беларусь", "Минск", "Востания", 121, 18)
adress("Момонтова", "Людмила", "Германия", "Дрезден", "Без названияя", 83, 11)

# +++++++++++++++++++++++++++++++++++++++++++++++++


def my_distance(x, y):
 distance = math.sqrt(x ** 2 + y ** 2)
 print(distance)


def their_distance(x_1, x_2, y_1, y_2):
 distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
 print(distance)


user_choice = int(
 input("Найти расстояние от себя до точки (1) или найти расстояние между двумя произвольными точками (2)? "))
if user_choice == 1:
 target_x = float(input("Введите координату X цели: "))
 target_y = float(input("Введите координату Y цели: "))
 my_distance(target_x, target_y)
elif user_choice == 2:
 target_x_1 = float(input("Введите координату X цели 1: "))
 target_y_1 = float(input("Введите координату Y цели 1: "))
 target_x_2 = float(input("Введите координату X цели 2: "))
 target_y_2 = float(input("Введите координату Y цели 2: "))
 their_distance(target_x_1, target_x_2, target_y_1, target_y_2)
else:
 print("Ввод неверный")
)

# +++++++++++++++++++++++++++++++++++++++++++++++++
def summ_n(num):
 summ_plus = 0
 for summ in range(1, num + 1):
  summ_plus += summ
 return summ_plus


boo = int(input("Введите число N: "))
print(f"\nСумма чисел введёного числа: {summ_n(boo)}")
two_boo = summ_n(boo)
print(f"\nСумма суммы чисел введёного числа: {summ_n(two_boo)}")


# +++++++++++++++++++++++++++++++++++++++++++++++++

def gcd(x, y):
 if x > y:
  small = y
 else:
  small = x
 gcd_find = 1
 for i in range(1, small + 1):
  if (x % i == 0) and (y % i == 0):
   gcd_find = i

 return gcd_find


first_number = int(input("Первое число: "))
second_number = int(input("Второе число: "))
print(f"НОД = {gcd(first_number, second_number)}")


# +++++++++++++++++++++++++++++++++++++++++++++++++

def numeral_count(number):
 count = 0
 while number:
  number //= 10
  count += 1
 return count


def numeral_check(n):
 max_count = 0
 max_number = 0
 for _ in range(1, n + 1):

  new_value = int(input("Введите число: "))
  if new_value < 0:
   new_value = 0

  cipher_count = numeral_count(new_value)
  if cipher_count > max_count:
   max_count = cipher_count
   max_number = new_value

 return max_number


how_many = int(input("Введите количество чисел: "))
print("Первая задача на обработку: ", numeral_check(how_many))

# ++++++++++++++++++++++++++++++++++++++++++++++++

count = 0
x = 1
while x != 0:
 x /= 2
 count += 1
 print(x)
print(count)

# ++++++++++++++++++++++++++++++++++++++++++++++++

num = float(input("Введите число в эксп. форме: "))
x = 1
count = 0
while x < 2:
 count += 1
 x += num
print(f"\nКол-во прибавлений: {count}")

# ++++++++++++++++++++++++++++++++++++++++++++++++

start_number = float(input("Введите число: "))
count = 0
while start_number > 10:
 count += 1
 start_number /= 10

print(f"Формат плавающей точки: x = {start_number} * 10 ** {count}")

##++++++++++++++++++++++++++++++++++++++++++++++++

tax = float(input("Общая сумма налога: "))
new_tax = float(input("Сумма нового налога: "))
while tax % 10 == 0:
 tax /= 10
 new_tax /= 10

if int(tax + new_tax) == int(tax):
 print("Бюджет не изменился")
else:
 print("Бюджет изменился")


# ++++++++++++++++++++++++++++++++++++++++++++++++

def eqv(a, b, c):
 return abs((a + b) - c) <= 1e-15


first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
third = float(input("Введите третье число: "))
print(eqv(first, second, third))

# ++++++++++++++++++++++++++++++++++++++++++++++++
index = input("Введите почтовый индекс: ")
for numb in index:
 if numb == "1" or numb == "2" or numb == "3" or numb == "4" or numb == "5" or numb == "6" or numb == "7" or numb == "8" or numb == "9" or numb == "0":
  print(numb, end='')


# ++++++++++++++++++++++++++++++++++++++++++++++++
# сумма чисел
def quantity_number(number_n):
 summ_plus = 0
 while number_n > 0:
  summ_plus += 1
  number_n //= 10
 return summ_plus


# ++++++++++++++++++++++++++++++++++++++++++++++++

#список степеней
numbers = [3,7,5]

while True:

 number = int(input('Новое число: '))

 numbers.append(number)

 print('Текущий список чисел:', numbers)

 for i in numbers:
   print(i ** 2, i ** 3, i ** 4)

 print()

 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 #список от 0 до 100

number = []
for _ in range(0,100 +1):
    number.append(_)

print(number)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#поиск по списку
list = []
numbers_of_workers = int(input("Сколько сотрудников в офисе?: "))
for _ in range(numbers_of_workers):
    ID_verification = int(input("Укажите Id сотрудника: "))
    list.append(ID_verification)
search_worker = int(input("Укажите Id сотрудника, которого ищем: "))
if search_worker not in list:
    print('Сотрудник не работает!')
else:
    print('Сотрудник на месте')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#мин макс через список
nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))

    nums_list.append(num)

maximum = nums_list[N-1]

minimum = nums_list[0]

for i in nums_list:

    if maximum < i:
        maximum = i

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

list = []
number = int(input("Кол-во чисел в списке: "))

for count in range(1, number +1):
    num_list = int(input(f"Введите {count}-е число: "))
    list.append(num_list)

divider = int(input(f"Введите делитель: "))
index = 0
sum_indexes = 0
for index, i_number in enumerate(list):
    if i_number % divider == 0:
        print(f"Индекс числа {i_number}: {index}")
        sum_indexes += index
print("Сумма индексов:", sum_indexes)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

if nums_list:
    maximum = nums_list[0]
    minimum = nums_list[0]

    minimum_index = 0
    maximum_index = 0
    for index, i in enumerate(nums_list):

        if maximum < i:
            maximum = i
            maximum_index = index

        if minimum > i:
            minimum = i
            minimum_index = index

    print('Максимальное число в списке:', maximum)
    print('Минимальное число в списке:', minimum)

    print(nums_list)
    nums_list[minimum_index], nums_list[maximum_index] = nums_list[maximum_index], nums_list[minimum_index]
    print(nums_list)
else:
    print('В списке нету чисел')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

user_msg = input("Введите строку: ")
letters = list(user_msg)
what_replace = ":"
for_what_replace = ";"
count = 0
for index, letter in enumerate(letters):
    if letter == what_replace:
        count += 1
        letters[index] = for_what_replace

for letter in letters:
    print(letter, end='')
print(f"\nКол-во замен: {count}")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
stroke = input("Введите строку: ")
num = int(input("Номер символа: "))
count = 0
check_stroke = list(stroke)
search = check_stroke[num-1]
search_plus = check_stroke[num-2]
search_minus = check_stroke[num]

print(f"Символ слева: {search_plus}")
print(f"Символ справа: {search_minus}")

if search is search_plus or search is search_minus:
    count += 1
    print(f"Есть ровно {count} такой же символ.")
else:
    print("Таких же символов нет.")
# ++++++++++++++++++
msg = input("Введите строку: ")
index_of_letter = int(input("Номер символа: ")) - 1  # сразу отнимаем 1, чтобы превратить номер в индекс
letters = list(msg)
count = 0
if index_of_letter > 0:
    print("Символ слева:", letters[index_of_letter - 1])
    if letters[index_of_letter - 1] == letters[index_of_letter]:
        count += 1
if index_of_letter < len(letters) - 1:
    print("Символ справа:", letters[index_of_letter + 1])
    if letters[index_of_letter + 1] == letters[index_of_letter]:
        count += 1

if count == 0:
    print("Таких же символов нет.")
elif count == 1:
    print("Есть ровно один такой же символ.")
elif count == 2:
    print("Таких символов два.")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
words_list = []
counts = [0, 0, 0]

for i in range(3):
    print("Введите", i+1, "слово", end=' ')
    word = input()
    words_list.append(word)

text = input("Слово из текста: ")
while text != "end":
    for index in range(3):
        if words_list[index] == text:
            counts[index] += 1
    text = input("Слово из текста: ")

print("Подсчёт слов в тексте")
for i in range(3):
    print(words_list[i], ':', counts[i])
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++