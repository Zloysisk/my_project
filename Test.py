list_container_weights = []
continer = int(input("Количество контейнеров: "))
for card_count in range(1, continer + 1):
    continer_num = int(input(f"Введите вес контейнера: "))
    if continer_num > 200 or continer_num < 0:
        print("Неравельно указан вес контейнера : не больше 200 кг, не может быть отрицательным ")
        continue
    list_container_weights.append(continer_num)
new_container_weight = int(input("Введите вес нового контейнера: "))

list_container_weights.append(new_container_weight)
print(list_container_weights)