'''
Plan:
	Create first page :Welcome
	Give choice for login between user and admin
	Do validation for admin
	Display appropriate messages for each user and admin
'''
#from prettytable import PrettyTable
from Class import Admin, Item, Food, Stationery, Cosmetic, Electronic, Book, Cloth, Cleaning, Utensil, Plastic, Sport, Bedding

template_string = "Sl.No\t\tName\t\tPrice\t\tQuantity\t\tDiscount"

cart = []

items_lst = [Food.all, Stationery.all, Cosmetic.all, Electronic.all, Book.all, Cloth.all, Cleaning.all, Utensil.all, Plastic.all, Sport.all, Bedding.all]

def validate(input):
	if (input == Admin.all[0].password):
		return True
	else:
		return False


def view_items(lst, inp):
	while True:
		category_lst = []
		print("Sl.No\t\tName\t\tPrice\t\tQuantity\t\tDiscount")
		i = 1
		for item in lst[inp - 1]:
			print(i,item.name, item.price, item.quantity, item.discount, sep = '\t\t')
			category_lst.append([i, item.name, item.price, item.quantity, item.discount, item])
		
		return category_lst


def view_categories():
	global item_lst
	i = 1
	print("Sl. No\t\tCategory")
	items_lst = [Food.all, Stationery.all, Cosmetic.all, Electronic.all, Book.all, Cloth.all, Cleaning.all, Utensil.all, Plastic.all, Sport.all, Bedding.all]
	for item_lst in items_lst:
		instance = item_lst[0]
		print(i,'\t\t',instance.__class__.__name__)
		i = i + 1


def view_items_to_add(lst):
	print("Sl.No\t\tName\t\tPrice\t\tQuantity\t\tDiscount")
	for item in lst:
		print(item[0],"\t\t", item[1], "\t\t", item[2], "\t\t", item[3], "\t\t", item[4])

def view_cart():
	global cart
	global template_string

	print(template_string)
	for item in cart:
		print(item[0],"\t\t", item[1], "\t\t", item[2], "\t\t", item[3], "\t\t", item[4])

def add_to_cart():

	pass

def remove_from_cart():
	pass

def purchase():
	pass

def print_bill():
	pass











user_choice = True

print("\t\tWELCOME TO AKSHAY SUPERMARKET!\n\n\n")
print("In the following steps please enter your choice by the number assigned to it\n\n")

while (user_choice == True):
	user_input = int(input("1. Customer Login\t\t\t2. Admin Login\t\t\t3. Exit\n\nChoice:"))
	print("\n\n\n")

	if user_input == 1:
		print("Greetings!\n\n\n")
		while True:
				user_input = int(input("1. View Categories\t\t2. View Cart\t\t 3. Home page\n\nChoice:"))
				if user_input == 1:
					while True:
						view_categories()
						user_input = int(input("\n\n\nEnter Sl. No to view items in category\n\nEnter 0 to go back\n\nChoice:"))
						if user_input == 1:
							category_lst = view_items(items_lst, user_input)
							user_input = int(input("\n\n\n1. Remove from cart\t\t2. Add to cart\t\t3. Exit\n\n\nChoice:"))
							if user_input == 1:
								pass
							elif user_input == 2:
								view_items_to_add(category_lst)
								user_input = int(input("1. Enter Sl No of element you want to add\t\t2. Exit\n\n\nChoice:"))
								if user_input == 1:
									sl_no = int(input("\n\nEnter the Sl.No of the item you want to add:\n\n"))
									qty = int(input("\n\nEnter the number of items you want to purchase:\n\n"))
									item = category_lst[sl_no - 1][5]
									item.quantity = item.quantity - qty
									cart.append([])
									add_to_cart()
								else:
									break
								
							else:
								break
						elif user_input == 2:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 3:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 4:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 5:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 6:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 7:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 8:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 9:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 10:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 11:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						else:
							break

				elif user_input == 2:
					view_cart()
					print("\n\n\n\n")
				else:
					break			

	elif user_input == 2:
		user_input = input("Enter Password:")
		user_input = validate(user_input)

		if (user_input == True):
			print("\n\n\nWelcome admin!\n\n")
			while True:
				user_input = int(input("1. View Categories\t\t2. View Profits\t\t 3. Logout\n\nChoice:"))

				if user_input == 1:
					while True:
						view_categories()
						user_input = int(input("\n\n\nEnter Sl. No to view items in category\n\nEnter 0 to go back\n\nChoice:"))
						if user_input == 1:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 2:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 3:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 4:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 5:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 6:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 7:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 8:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 9:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 10:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 11:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						else:
							break
				elif user_input == 2:
					pass
				else:
					print("\n\n\nLogging out...\n\n\n")
					break

		else:
			print("\n\n\nWrong password...redirecting to home page\n\n\n")

	else:
		break 
