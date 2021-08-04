class Bag:
    count = 0
    def __init__(self):
        Bag.count += 1

    @classmethod
    def sell(cls):
        cls.count -= 1

    @classmethod
    def remain_bag(cls):
        return cls.count

print('Current bag: {}'.format(Bag.remain_bag()))
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('Current bag: {}'.format(Bag.remain_bag()))
bag1.sell()
bag2.sell()
print('Current bag: {}'.format(Bag.remain_bag()))
