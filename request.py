class Request:
    def __init__(self, string_):
        list_ = self.get_data(string_)
        self.from_ = list_[4]
        self.to = list_[6]
        self.amount = int(list_[1])
        self.product = list_[2]

    def get_data(self, string_):
        return string_.split(" ")

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_}а в {self.to}"
