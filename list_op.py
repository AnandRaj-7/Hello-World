food = ["rice","beans"]
print("The original list is ",food)
food.append("broccoli")
print("The list after appending an item to the list is ",food)
food.extend(["bread","pizza"])
print("The list after using extend method to append two items to the list is ",food)
print("The first two items in the list are ",food[:2])
print("The last item in the list is ",food[4])
breakfast = "eggs, fruit, orange juice"
breakfast = breakfast.split(", ")
print("The original breakfast list is ",breakfast)
print("The number of items in the list breakfast is ",len(breakfast))