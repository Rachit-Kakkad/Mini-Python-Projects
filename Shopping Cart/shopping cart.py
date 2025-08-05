#shopping cart list

food_items = []
price = []
total = 0

while True:
    food = input("Enter your food item which you want to buy {enter q to exit} : ")
    if food.lower() == "q":
        break

    else:
        item_price = float(input(f"Enter the price of {food} : Rs. "))
        food_items.append(food)
        price.append(item_price)

print("---------------  YOUR LISTED CART ITEMS ARE  ---------------")

for food_item in food:
    
 print(food_items, end=" ")

if item_price in price: 

 total += price
 
 print(f"Your total is {total} Rs.")
