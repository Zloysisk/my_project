print("Что бы управлять марсоходом введите: север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D)")
coordinat_x = 8
coordinat_y = 10
while True:
  move = input(f"\nМарсоход находится на позиции {coordinat_x}, {coordinat_y}, введите команду: ")
  if coordinat_x == 15 or coordinat_x == 0: 
    print ("Вы упёрилсь в стенку и отошли назад")
    if coordinat_x == 0:
      coordinat_x += 1
    elif coordinat_x == 15:
      coordinat_x -= 1
    continue
  elif coordinat_y == 20 or coordinat_y == 0: 
    print ("Вы упёрилсь в стенку и отошли назад")
    if coordinat_y == 0:
      coordinat_y += 1
    elif coordinat_y == 20:
      coordinat_y -= 1
    continue
  if move == "w": 
    coordinat_x += 1 
  elif move == "s": 
    coordinat_x -= 1
  elif move == "d": 
    coordinat_y += 1
  elif move == "a": 
    coordinat_y -= 1