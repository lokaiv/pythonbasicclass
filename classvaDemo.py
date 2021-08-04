class Korean:
    country = "korea"

    # def __init__(self, name, age, address):
        # self.name = name
        # self.age = age
        # self.address = address


# man = Korean('Kimminsu', 35, 'seoul')
# weman = Korean('Julie', 47, 'seoul')


# Korean.name   error
# print(man.name)
#print(Korean.country)
# print(man.country)
# print(man.age)
# print(man.address)


# print(weman.name)
# print(weman.country)
# print(weman.age)
# print(weman.address)

    @classmethod   # decorator
    def trip(cls, country):
        if cls.country == country:
            print("domestic")
        else:
            print("abroad")

Korean.trip('korea')
Korean.trip('usa')