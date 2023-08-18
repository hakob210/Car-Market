import datetime
from car import Car

class Person:

  seller_balance = 0
  
  def __init__(self, name, surname, city):
    self.name = name
    self.surname = surname
    self.city = city

class Seller(Person):
  def __init__(self, name, surname, city):
    super().__init__(name, surname, city)

  def __str__(self):
    return f"{self.name} {self.surname} from the city of {self.city}"

class Buyer(Person):
  
  def __init__(self, name, surname, city, money):
    super().__init__(name, surname, city)
    self.money = money
    self.spent_money = 0
    self.bought_cars = []

  def __str__(self):
    return f"{self.name} {self.surname} from {self.city}"

  def check_balance(self):
    print(f"Your Balance: {self.money}")

  def print_my_cars(self):
    if self.bought_cars:
      print(f"\n{self.name}'s purchased cars:")
      bc_index = 0
      for car_info in self.bought_cars:
        bc_index += 1
        print(f"\nCar number {bc_index}")
        print(f"\nMake: {car_info['make']}")
        print(f"Model: {car_info['model']}")
        print(f"Date: {car_info['date']}")

    else:
      print(f"\n{self.name} {self.surname} hasn't bought any cars.")

  def buy(self, car, date):
    if self.money >= car.price:
      amount_paid = car.price
      self.money -= amount_paid
      car.sell(self, date, applied_discount = True)
      self.add_bought_car(car, date)
      Car.cars.remove(car)
      Person.seller_balance += car.price
      
    else:
      print("Not enough money")

  def add_bought_car(self, car, date):
    bought_car_info = {
      'make': car.make,
      'model': car.model,
      'year': car.year,
      'price': car.price,
      'discount': car.discount,
      'date': date
    }
    self.bought_cars.append(bought_car_info)
    self.spent_money += car.price

  def return_car(self, car, reason_of_return):
    self.money += car['price'] - car['discount']
    Car(car['make'], car['model'], car['year'], car['price'])
    Person.seller_balance -= car['price']