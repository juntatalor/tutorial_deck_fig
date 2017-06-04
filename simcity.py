class City:
    def __init__(self, name):
        self.name = name
        self.streets = {}

    def __str__(self):
        return self.name

    @property
    def population(self):
        # Популяция дома - сумма популяций улиц
        return sum(street.population for street in self.streets.values())

    def add_street(self, name):
        street = Street(self, name)
        self.streets[name] = street
        return street

    def remove_street(self, name):
        del self.streets[name]


class Street:
    def __init__(self, city, name):
        self.city = city
        self.name = name
        self.houses = {}

    def __str__(self):
        return str(self.city) + ', ' + str(self.name)

    @property
    def population(self):
        # Популяция улицы - сумма популяции домов на ней
        return sum(house.population for house in self.houses.values())

    def add_house(self, name, population):
        house = House(self, name, population)
        self.houses[name] = house
        return house


class House:
    def __init__(self, street, name, population):
        self.name = name
        self.street = street
        self.population = population

    def __str__(self):
        return str(self.street) + ', ' + str(self.name)
