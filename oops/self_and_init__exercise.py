class House:
    #price = 1000000
    def __init__(self, bedrooms, hall, kitchen, location_type, neighbourhood_class, price):
        self.bedrooms = bedrooms
        self.hall = hall
        self.kitchen = kitchen
        self.location_type = location_type
        self.neighbourhood_class = neighbourhood_class
        self.price = price

    def price_modified(self):    
        if self.location_type == 'city':
            price_1 = self.price
        elif self.location_type == 'town':
            price_1 = self.price - 250000    

        if self.neighbourhood_class == 'rich':
            self.price_2 = price_1 + 250000
        elif self.neighbourhood_class == 'middle':
            self.price_2 = price_1
        else:
            self.price_2 = price_1 - 250000
        return self.price_2

    def price_of_house(self):
        bedrooms = self.bedrooms
        hall = self.hall
        kitchen = self.kitchen
        price_3 = self.price_modified()
        house_price = price_3 * (bedrooms + 1.1*hall + 0.9*kitchen)
        print(f'The Price of the house is {house_price}')

my_house = House(2,2,1,'town','middle', 150000)

my_house.price_of_house()

