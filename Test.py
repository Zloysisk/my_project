names = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]



for count in range(0,len(names)):
    if count % 2 != 0:
        print(names[count], end= " ")
