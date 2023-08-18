import datetime
from person import Person, Seller, Buyer
from car import Car


car1 = Car("Toyota", "Camry", 2022, 25000)
car2 = Car("Ford", "Mustang", 2019, 45000)
car3 = Car("Chevrolet", "Corvette", 2020, 65000)
car4 = Car("Honda", "Civic", 2021, 22000)
car5 = Car("BMW", "M3", 2023, 65000)
car6 = Car("Audi", "A4", 2018, 40000)
car7 = Car("Nissan", "GT-R", 2017, 120000)
car8 = Car("Porsche", "911", 2022, 90000)
car9 = Car("Lamborghini", "Aventador", 2019, 400000)
car10 = Car("Ferrari", "488 GTB", 2020, 300000)
car11 = Car("Maserati", "Quattroporte", 2021, 120000)
car12 = Car("Jaguar", "F-PACE", 2018, 50000)
car13 = Car("Kia", "Telluride", 2023, 35000)
car14 = Car("Volvo", "XC90", 2019, 55000)
car15 = Car("Subaru", "Outback", 2021, 27000)



class Console:
  def __init__(self):
    self.cars = Car.cars
    

  def run_seller(self):
    print("\nSELLER")
    name = input("\nEnter your name: ")
    surname = input("Enter your surname: ")
    city = input("Enter your city: ")

    seller = Seller(name, surname, city)

    while True:
      print("\nSELLER")
      print("1. View available cars")
      print("2. Set discount for a car")
      print("3. Check balance")
      print("4. Exit menu")

      choice = input("Enter your action: ")

      if choice == "1":
        Car.get_seller_available_cars()
      elif choice == "2":
        car_choice = int(input("Enter the car number you want to pick: "))
        car = Car.cars[car_choice - 1]
        discount = float(input("Set a discount: "))
        car.set_discount(discount)
        print(f"\nSet discount of {discount} on {car.make} {car.model}")
      elif choice == "3":
        print(f"\nYour balance: {Person.seller_balance}")
      elif choice == "4":
        break
      else:
        print("Invalid option")

  def run_buyer(self):
    print("\nBUYER")
    name = input("\nEnter your name: ")
    surname = input("Enter your surname: ")
    city = input("Enter your city: ")
    money = float(input("Enter your available money: "))

    buyer = Buyer(name, surname, city, money)

    while True:
      print("\nBuyer's actions:")
      print("1. View available cars")
      print("2. Buy a car")
      print("3. Print my cars")
      print("4. Return a car")
      print("5. Check balance")
      print("6. Exit This Menu")

      choice = input("Enter your action: ")

      if choice == "1":
        Car.get_seller_available_cars()
      elif choice =="2":
        car_choice = int(input("Enter the car number you want to buy: "))
        car = self.cars[car_choice - 1]
        current_date = datetime.date.today()
        buyer.buy(car, current_date.strftime("%d.%m.%Y"))
      elif choice =="3":
        buyer.print_my_cars()
      elif choice =="4":
        car_choice = int(input("The number of the car you want to return: "))
        reason = input("Reason of return: ")
        car_info = buyer.bought_cars[car_choice - 1]
        buyer.return_car(car_info, reason)
        print(f"The car is returned back to the market because of {reason}.")
      elif choice == "5":
        buyer.check_balance()
      elif choice == "6":
        break
      else:
        print("Invalid option")

  def run(self):
    print("Welcome to the car market!")

    while True:
      print("\nSelect an option:")
      print("1. I'm a seller")
      print("2. I'm a buyer")
      print("3. Exit")

      choice = input("Your choice: ")

      if choice == "1":
        self.run_seller()
      elif choice == "2":
        self.run_buyer()
      elif choice == "3":
        print("You exited the market. Goodbye!")
        break
      else:
        print("Invalid choice.")

start = Console()
start.run()