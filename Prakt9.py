CARS_COUNT = 5
PASSENGER_TYPE = "легковий"

cars = {}

for car_number in range(CARS_COUNT):
    print("Автомобіль", car_number + 1)

    model = input("Назва моделі: ")
    car_type = input("Тип (легковий/вантажний): ")
    price = float(input("Вартість: "))

    cars[model] = (car_type, price)

# Виведення словника
print("\nВсі дані:")
for model, car_info in cars.items():
    print(model, "->", car_info)

total_price = 0
passenger_count = 0

for model, car_info in cars.items():
    car_type, price = car_info
    if car_type.lower() == PASSENGER_TYPE:
        total_price += price
        passenger_count += 1

if passenger_count > 0:
    average_price = total_price / passenger_count
    print("\nСередня вартість легкових автомобілів:", average_price)
else:
    print("\nЛегкових автомобілів немає")

print("\nДодавання нового запису")

new_model = input("Назва моделі: ")
new_type = input("Тип: ")
new_price = float(input("Вартість: "))

cars[new_model] = (new_type, new_price)

model_to_delete = input("\nЯку модель видалити: ")

if model_to_delete in cars:
    del cars[model_to_delete]
    print("Запис видалено")
else:
    print("Такої моделі немає")

print("\nСловник за відсортованими ключами:")

for model in sorted(cars.keys()):
    print(model, "->", cars[model])
