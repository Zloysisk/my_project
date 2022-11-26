
print('=======================================================================================')
print("Вас приветствует 'Zloysisk's Автозаменьщик'")
print('\nПишите текст по одому слову на латинской раскладке, в ответ получите текcт на кирилице"')
print('=======================================================================================')
while True:
  wrong = input('\nТекст: ')
  if wrong == "end":
    break
  wrong_list = list(wrong)
  #print(wrong_list)
  count = 0


  en = []
  proto_en = ("qwertyuiop[]asdfghjkl;'\zxcvbnm,.")
  en.extend(proto_en)

  rus = []
  proto_rus = ("йцукенгшщзхъфывапролджэёячсмитьбю")
  rus.extend(proto_rus)



  for count_w, value_w in enumerate(wrong_list):      
    for count, value in enumerate(en):
      if value == value_w:
        print(f"{rus[count]}", end = "")
  continue


  #print(len(en))
  #print(len(rus))
    

  #print(en)
  #print(rus)