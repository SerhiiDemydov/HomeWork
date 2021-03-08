# 3. Make class with one method
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """
    @staticmethod
    def add_nums(a, b, c):
        return a + b + c


print(f'Sum = {Calc.add_nums(10, 5, 6)}')



# 4*.
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

    def __init__(self, ingredient):
        self.ingredient = ingredient

    @classmethod
    def carborano(cls):
         return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(['forcemeat', 'tomatoes'])
print(pasta_1.ingredient)
pasta_2 = Pasta.carborano()
print(pasta_2.ingredient)
pasta_3 = Pasta.bolognaise()
print(pasta_3.ingredient)


# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, x):
        if x > self.max_visitor_num:
            self._visitors_count = self.max_visitor_num
        else:
            self._visitors_count = x


Concert.max_visitor_num = 50
concert = Concert()
print(concert.__dict__)
concert.visitors_count = 100
print(concert.visitors_count)



