new_word = input('Введите слово: ')
word = list(new_word)
count = 0
word.sort()
for check in word: 
    for check_2 in word: 
        if check == check_2: 
            count += 1
print(count)