#Lecture 3 Example 2
# 1) Review the code and predict what the value of each variable will be on each line,
# and then predict the output of the print statements without executing any of the code.

# 2) Next, practice using PyCharm's debugger by stepping through each line of code
# to verify your previous predictions.

inventory = [
    "tent",
    "water",
    "flashlight",
    "snacks"
]

water_bottles = 3
days = 2

food_items = len(inventory) - 2 # 2

enough_water = water_bottles >= days * 2 # False
has_light = "flashlight" in inventory # True
has_shelter = "tent" in inventory # True

ready_to_camp = (
    enough_water # False
    and has_light # True
    and has_shelter # True
) # False

inventory = inventory + ["first aid kit"] #[tent, water, flashlight, snacks]

water_bottles += 2 # 5

enough_water = water_bottles >= days * 2 # True


food_items = len(inventory) - 2 # 3

trip_score = 0

trip_score += 25*has_shelter # 25
trip_score += 25*has_light # 50
trip_score += 25*enough_water # 75
trip_score += 25*(food_items >= 1) # 100

print(inventory)
print(trip_score)
print(ready_to_camp)
print(enough_water)