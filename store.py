from storage import Storage


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def __repr__(self):
        return "склад"

    def add(self, name: str, count: int):
        is_item_found = False  # Проверяем, найдено ли наименование товара на складе
        if self.get_free_space() >= count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_item_found = True
            if not is_item_found:
                self.items[name] = count
                print(f"Товар {count} {name} добавлен в {self}")
        else:
            if self.get_free_space() == 0:
                print("На складе закончилось место, товар не может быть добавлен")
            else:
                print(f"Не хватает свободного места на складе. Можно добавить только {self.get_free_space()} товаров")

    def remove(self, name: str, count: int):
        is_item_found = False
        for key in self.items.keys():
            if name == key:
                is_item_found = True
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Нет нужного количества {name}")
        if not is_item_found:
            print("Такого товара нет складе")

        if self.items[name] == 0 and is_item_found:
            del self.items[name]

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def unique_items_count(self):
        return len(self.items.keys())
