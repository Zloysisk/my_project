SEPARATOR = '------------------------------------------'

#user info  
name = ""
age = 0
tel = ""
email = ""
index = ""
adress = ""
another_info = ""

#company info
ogrnip = ""
inn = ""
curent_acc = ""
bank_name = ""
bic = ""
cor_acc = ""



def correct_age(age):
  if 11 <= age % 100 <= 19: 
    years_name = 'лет'
  elif age % 10 == 1: 
    years_name = 'год'
  elif 2 <= age % 10 <= 4: 
    years_name = 'года'
  else: 
    years_name = 'лет'
  return years_name

def correct_index(index): 
  numb_index = " "
  for numb in index: 
    if numb == "1" or numb == "2" or numb == "3" or numb == "4" or numb == "5" or numb == "6" or numb == "7" or numb == "8" or numb == "9" or numb == "0":
      numb_index += numb
  return numb_index
       


def self_info_out():
  print(f"\nИмя: {name}\nВозраст: {age} {correct_age(age)}\nТелефон: {tel} \nE-mail: {email}\nИндекс:{correct_index(index)}  \nАдрес (без индекса): {adress}")
  if another_info:
    print(f"Дополнительная информация: \n{another_info}")

def company_info_out():
  print(f"\nИнформация о предпринимателе\nОГРНИП:{ogrnip} \nИНН:{inn}\nБанковские реквизиты \nР/с:{curent_acc} \nБанк:{bank_name} \nБИК:{bic} \nК/с:{cor_acc}") 

print("Приложение MyProfile для предпринимателей")
print("Сохраняй информацию о себе и выводи ее в разных форматах")


while True:
  # main menu
  print(SEPARATOR)
  print("ГЛАВНОЕ МЕНЮ")
  print("1 - Ввести или обновить информацию")
  print("2 - Вывести информацию")
  print("0 - Завершить работу")
  
  option = int(input("\nВведите номер пункта меню: "))
  if option == 0:
    break
  #ввод информции
  elif option == 1:
    while True:
      print(SEPARATOR)
      print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
      print('1 - Личная информация')
      print('2 - Информация о предпринимателе')
      print('0 - Назад')
      option2 = int(input("Введите номер пункта меню: "))
      if option2 == 0:
        break
      #личная информация  
      elif option2 == 1:
        name = str(input("Введите имя: "))
        while 1:
          age = int(input("Введите возраст: "))
          if age > 0: 
            break
          print("Возраст должен быть положительным")
        tel = str(input("Введите номер телефона (+7ХХХХХХХХХХ): "))
        email = str(input("Введите адрес электронной почты: "))
        index = str(input("Введите почтовый индекс: "))
        
        adress = str(input("Введите почтовый адрес (без индекса): "))
        another_info = str(input("Введите дополнительную информацию: "))
        
      #инфа о компании  
      elif option2 == 2:
        while 2:  
          ogrnip = int(input("Введите ОГРНИП: "))
          checking = 0
          check = ogrnip
          while check > 0:
            checking += 1
            check //= 10
          if checking < 15: 
            print("ОГРНИП должен содержать 15 цифр")
            continue
          else:
            break
            
        inn = int(input("Введите ИНН: "))
        
        while 2:
          curent_acc = int(input("Введите расчетный счет: "))
          checking = 0
          check = curent_acc
          while check > 0:
            checking += 1
            check //= 10
          if checking < 20: 
            print("Р/с должен содержать 20 цифр")
            continue
          else:
            break
        bank_name = str(input("Введите название банка: "))
        bic = int(input("Введите БИК: "))
        cor_acc = int(input("Введите корреспондентский счёт: "))
        
  #меню вывода информации    
  elif option == 2:
    while True:
      print(SEPARATOR)
      print("ВЫВЕСТИ ИНФОРМАЦИЮ")
      print("1 - Общая информация")
      print("2 - Вся информация")
      print("0 - Назад")
      option2 = int(input("Введите номер пункта меню: "))
      #вывод информации
      if option2 == 0:
        break
      if option2 == 1:
        self_info_out()
      if option2 == 2:
        self_info_out()
        company_info_out()
  else:
    print("\nВведите корректный пункт меню")