original_list = []
amount = int(input("Введите количество цифр в строчке: "))
for _ in range(amount):
    numbers = int(input("Введите числа в строчку: "))
    original_list.append(numbers)
shift = int(input("На сколько сдивнуть строку? : "))



actual_count = shift * -1
shifted_list = [[numb for numb in original_list[actual_count + len(original_list): ]],[numb for numb in original_list[ :len(original_list) - shift]]]
shifted_list = [count for numb_3 in shifted_list for count in numb_3]


print(shifted_list)


#shifted_list = []
#for numb in (original_list[actual_count + len(original_list): ]):   #те, что переносятся
    #shifted_list.append(numb)
#for numb in (original_list[ :len(original_list) - shift]):        # те, что остаются
    #shifted_list.append(numb)
#shifted_list = [numb for numb in original_list[actual_count + len(original_list): ]]
#shifted_list.append(original_list[:len(original_list) - shift])
#shifted_list.append(original_list[actual_count +len(original_list):])
