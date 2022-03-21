from store import Store


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 20
        self._limit = limit

    def __repr__(self):
        return "магазин"

    @property
    def limit(self):
        return self._limit

    def add(self, name: str, count: int):
        if self.unique_items_count() <= self._limit:
            super().add(name, count)
        else:
            print("Товар не может быть добавлен")
