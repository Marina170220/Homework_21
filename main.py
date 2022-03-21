from shop import Shop, Store
from request import Request

if __name__ == "__main__":
    shop = Shop()
    shop.add("печеньки", 4)
    shop.add("пряники", 3)
    shop.add("плюшки", 5)
    shop.add("ватрушки", 4)
    store = Store()
    store.add("печеньки", 10)
    store.add("плюшки", 10)
    store.add("крендельки", 4)

    user_input = input()  # Пользовательский ввод в формате Доставить 6 крендельки из склад в магазин
    user_input_list = user_input.split(" ")
    is_input_correct = True
    try:
        user_input_list[1] = int(user_input_list[1])
    except:
        print("Введите целое число")
        is_input_correct = False
    if ("доставить" or "забрать") not in user_input_list[0].lower():
        print("Введите доставить или забрать")
        is_input_correct = False
    if ("магазин" and "склад") not in user_input_list[4].lower():
        print(" Введите магазин или склад")
        is_input_correct = False

    if is_input_correct:
        request = Request(user_input)
        print(request)
        if "магазин" in request.from_.lower():
            print("Можно доставить только со склада")
        elif "склад" in request.from_.lower():
            if request.product in store.get_items():
                if request.amount <= store.get_items()[request.product]:
                    print(f"Нужное количество есть на {request.from_}е")
                    print(f"Курьер забрал {request.amount} {request.product} из {request.from_}а")
                    print(f"Курьер везёт {request.amount} {request.product} из {request.from_}а в {request.to}")
                    if sum(shop.get_items().values()) + int(request.amount) <= shop.capacity:
                        print(f"Курьер доставил {request.amount} {request.product} из {request.from_}а в {request.to}")
                        store.remove(request.product, request.amount)
                        shop.add(request.product, request.amount)
                    else:
                        print(f"В {request.to}е недостаточно места. Попробуйте изменить запрос.")
                else:
                    print(
                        f"На {request.from_}е нет нужного количества {request.product}. Попробуйте изменить количество.")
            else:
                print("Такого товара нет на складе")

        if shop.unique_items_count():
            print("\nВ магазине хранится:\n")
            for key, value in shop.items.items():
                print(key, value)
        else:
            print("\nВ магазине пусто")

        if store.unique_items_count():
            print("\nНа складе хранится:\n")
            for key, value in store.items.items():
                print(key, value)
        else:
            print("\nНа складе пусто")
