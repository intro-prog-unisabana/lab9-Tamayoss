# Write your class definition here!
class Car:
    def __init__(self, car_id, brand, year, color, mileage=0.0):
        self.car_id=car_id
        self.brand=brand
        self.year=int(year)
        self.color=color
        self.mileage=float(mileage)
    def change_color(self, new_color):
        self.color = new_color
    def drive(self, miles):
        self.mileage=miles+self.mileage
    def __str__(self):
        return f"{self.car_id} - {self.year} {self.color} {self.brand} with {self.mileage} miles"

