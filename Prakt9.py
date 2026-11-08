CARS_COUNT = 5
PASSENGER_TYPE = "легковий"


def input_car(type_prompt):
    model = input("Назва моделі: ")
    car_type = input(type_prompt)
    price = float(input("Вартість: "))
    return model, car_type, price


def read_cars(count):
    cars = {}
    for car_number in range(count):
        print("Автомобіль", car_number + 1)
        model, car_type, price = input_car("Тип (легковий/вантажний): ")
        cars[model] = (car_type, price)
    return cars


def print_cars(cars):
    for model, car_info in cars.items():
        print(model, "->", car_info)


def calculate_average_price(cars, wanted_type):
    total_price = 0
    count = 0
    for car_type, price in cars.values():
        if car_type.lower() == wanted_type:
            total_price += price
            count += 1
    if count == 0:
        return None
    return total_price / count


def delete_car(cars, model):
    if model in cars:
        del cars[model]
        return True
    return False


def main():
    cars = read_cars(CARS_COUNT)

    print("\nВсі дані:")
    print_cars(cars)

    average_price = calculate_average_price(cars, PASSENGER_TYPE)
    if average_price is not None:
        print("\nСередня вартість легкових автомобілів:", average_price)
    else:
        print("\nЛегкових автомобілів немає")

    print("\nДодавання нового запису")
    model, car_type, price = input_car("Тип: ")
    cars[model] = (car_type, price)

    model_to_delete = input("\nЯку модель видалити: ")
    if delete_car(cars, model_to_delete):
        print("Запис видалено")
    else:
        print("Такої моделі немає")

    print("\nСловник за відсортованими ключами:")
    print_cars(dict(sorted(cars.items())))


main()
