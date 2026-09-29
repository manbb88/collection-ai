class MyZoo:
    def __init__(self, animals=None):
        print("My Zoo!")
        if animals is None:
            self.animals = {}
        else:
            self.animals = animals

    def __str__(self):
        return str(self.animals)

    def __eq__(self, other):
        if not isinstance(other, MyZoo):
            return NotImplemented
        return set(self.animals.keys()) == set(other.animals.keys())

    def __len__(self):
        # len(对象) 输出所有动物总数
        return sum(self.animals.values())