food=["rice","beans"]
print(f"The original food list is ",food)
food.append("broccoli")
print(f"The appended food list is ",food)
food.extend(["bread","pizza"])
print(f"The extended new list of food is ",food)
print(f"The food item at first 2 indices are",food[0:2])
print(f"The food item at the last position is {food[-1]}")
breakfast = list("eggs, fruit, orange, juice".split(", "))
print(breakfast)
print("The breakfast list has 3 items is",len(breakfast) is 3)
animals = ["lion", "tiger", "frumious Bandersnatch"]
print(animals)
large_cats = animals
print(large_cats)
large_cats.append("Tigger")
print(animals) # large_cats and animals both are 2 different names of the same memory address so btoh print the same list
print(large_cats)