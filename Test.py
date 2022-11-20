list_container_weights = []
continer = int(input("Количество контейнеров: "))
for card_count in range(1, continer + 1):
    continer_num = int(input(f"Введите вес контейнера: "))
    if continer_num > 200 or continer_num < 0:
        print("Неравельно указан вес контейнера : не больше 200 кг, не может быть отрицательным ")
        continue
    list_container_weights.append(continer_num)

new_container_weight = int(input("Введите вес нового контейнера: "))

for count, weights in enumerate(list_container_weights): 
    if weights > new_container_weight: 
        list_container_weights.insert(count, new_container_weight)


print(list_container_weights)