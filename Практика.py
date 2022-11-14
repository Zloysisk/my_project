wrong = input('Текст: ')
wrong_list = list(wrong)
# print(wrong_list)
count = 0
en = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "<", "p", "[", "]", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";",
      "'", "z", "x", "c", "v", "b", "n", "m", ","]

rus = ["й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж",
       "э", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю"]

# print(len(en))
# print(len(rus))


print(en[12])
print(rus[12])

for count, value in enumerate(en):
    for count_w, value_w in enumerate(wrong_list):
        if value == value_w:
            print(f"{rus[count]}", end="")

