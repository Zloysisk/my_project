number = int(input('Введите число: '))
denary = -1
while True:
  denary += 1
  number //= 10
  if number == 0: 
    break
print('Количество десятичных цифр ', denary)