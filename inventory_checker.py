print("Sneaker Inventory Checker")

shoe_name = input("Enter the Shoe Name: ")
quantity = int(input("Enter the quantity of the shoe that is in stock: "))

if quantity == 0:
  print(shoe_name, "is out of stock, make sure to get more soon.")
elif quantity <= 3:
      print(shoe_name, "is running low, look into getting more.")
else:
   print(shoe_name, "has sufficient inventory.")
