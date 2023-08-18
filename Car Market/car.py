import datetime

class Car:
  
  cars = []
  
  def __init__(self, make, model, year, price):
    self.make = make
    self.model = model
    self.year = year
    self.price = price
    self.sold = False
    self.sold_history = []
    self.lastSoldIndex = None
    self.discount = 0
    Car.cars.append(self)

  def set_discount(self, discount):
    self.discount = discount
    self.price -= discount

  def sell(self, buyer, date, applied_discount = False):
    self.sold = True
    self.sold_history.append({
      'buyer' : buyer,
      'price' : self.price,
      'date' : date,
      'discount' : self.discount if applied_discount else 0,
      'returned' : False,
      'reason_of_return' : None
    })

    self.lastSoldIndex = len(self.sold_history) - 1
    print(f"\n{self.make} {self.model} sold to {buyer} for {self.price - self.discount:.2f}$")

  def get_sold_car_history(self, seller_name):
    sold_car_history = []
    for car in Car.cars:
      if car.seller == seller_name and car.sold:
        for sold_entry in car.sold_history:
          car_info = {
            'seller': car.seller,
            'make': car.make,
            'model': car.model,
            'year': car.year,
            'buyer': sold_entry['buyer'],
            'price': sold_entry['price'],
            'date': sold_entry['date'],
            'discount': sold_entry['discount'],
            'returned': sold_entry['returned'],
            'reason_of_return': sold_entry['reason_of_return']
          }
          sold_car_history.append(car_info)
    return sold_car_history
    
  def get_seller_available_cars():
    print("\nAvailable cars:")
    count = 0
    av_cars = []
    for car in Car.cars:
      count += 1
      av_cars.append(f"{count}. {car.make} {car.model}, {car.year}, Price: {car.price}$")
    for c in av_cars:
      print(c)