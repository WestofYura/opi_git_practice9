n = 5

cars = {}

for i in range(n):
    print("Автомобіль", i + 1)

    model = input("Назва моделі: ")
    car_type = input("Тип (легковий/вантажний): ")
    price = float(input("Вартість: "))

    cars[model] = (car_type, price)

# Виведення словника
print("\nВсі дані:")
for model, info in cars.items():
    print(model, "->", info)

sum_price = 0
count = 0

for model, info in cars.items():
    if info[0].lower() == "легковий":
        sum_price += info[1]
        count += 1

if count > 0:
    average = sum_price / count
    print("\nСередня вартість легкових автомобілів:", average)
else:
    print("\nЛегкових автомобілів немає")

print("\nДодавання нового запису")

new_model = input("Назва моделі: ")
new_type = input("Тип: ")
new_price = float(input("Вартість: "))

cars[new_model] = (new_type, new_price)

delete_model = input("\nЯку модель видалити: ")

if delete_model in cars:
    del cars[delete_model]
    print("Запис видалено")
else:
    print("Такої моделі немає")

print("\nСловник за відсортованими ключами:")

for model in sorted(cars.keys()):
    print(model, "->", cars[model])