class Admin:
	def __init__(self, password: str):
		self.password = password

class Item:
	discount = 0.2
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		assert price >= 0, f"Price {price} is not greater than 0!"
		assert quantity >= 0, f"Price {quantity} is not greater than 0!"

		self.name = name
		self.price = price 
		self.quantity = quantity
		Item.all.append(self) 
	
	
	def __repr__(self): 
		return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


	def calculate_total_price(self): 
		return self.quantity * self.price

	def apply_discount(self):
		self.price = self.price - (self.price * self.discount)

class Food(Item):
	discount = 0.15
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)

		Food.all.append(self)

class Stationery(Item):
	discount = 0.1
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Stationery.all.append(self)

class Cosmetic(Item):
	discount = 0.15
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Cosmetic.all.append(self)

class Electronic(Item):
	discount = 0.3
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Electronic.all.append(self)

class Book(Item):
	discount = 0.1
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Book.all.append(self)

class Cloth(Item):
	discount = 0.3
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Cloth.all.append(self)

class Cleaning(Item):
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Cleaning.all.append(self)

class Utensil(Item):
	discount = 0.25
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Utensil.all.append(self)

class Plastic(Item):
	discount = 0.1
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Plastic.all.append(self)


class Sport(Item):
	discount = 0.05
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Sport.all.append(self)

class Bedding(Item):
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Bedding.all.append(self)

class Toiletery(Item):
	discount = 0.1
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Toiletery.all.append(self)


food1 = Food("Lays Chips", 20, 10)
'''
food2 = Food("Dairy Milk", 20, 10)
food3 = Food("Tropicana", 50, 10)
food4 = Food("Hide&Seek", 30, 10)
food5 = Food("Aloo Bhujia", 40, 10)
'''
stationery1 = Stationery("Pilot V5", 70, 10)
'''
stationery2 = Stationery("Apsara Pencil", 50, 10)
stationery3 = Stationery("Kangaro Stapler", 30, 10)
stationery4 = Stationery("Nataraj Sharpener", 50, 10)
stationery5 = Stationery("Pilot Marker", 100, 10)
'''
cosmetic1 = Cosmetic("Lakme Lotion", 70, 10)
'''
cosmetic2 = Cosmetic("Dove Soap", 40, 10)
cosmetic3 = Cosmetic("Tresseme Hair Conditioner", 100, 10)
cosmetic4 = Cosmetic("Dettol Soap", 80, 10)
cosmetic5 = Cosmetic("", 70, 10)
'''
electronic1 = Electronic("Charger", 500, 10)

book1 = Book("Classmate", 100, 10)

cloth1 = Cloth("Gloves", 100, 10)

cleaning1 = Cleaning("SurfXL", 100, 10)

utensil1 = Utensil("Bottle", 250, 10)

plastic1= Plastic("Bucket", 200, 10)

sport1 = Sport("Football", 300, 10)

bedding1 = Bedding("Pillow", 100, 10)

for item in Item.all:
	print(item)






