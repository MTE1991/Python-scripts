print("""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
""")
#List:
print("This is a list:")
car_brands = ["Ferrari", "Toyota", "Nissan", "Buggati", "Honda", "Lotus"]
print(car_brands)

for x in car_brands:
    print(x)

#list length:
print("The length of this list is:")
print(len(car_brands))

print(car_brands[0]) #1st item (index 0)
print(car_brands[1]) #2nd item

#Negative indexing:
print(car_brands[-1]) #1st from bottom

print(car_brands[1:3]) #index 1 to index 3
print(car_brands[1:]) #index 1 to end
print(car_brands[:5])

#Append
car_brands.append("Porsche")
print(car_brands)

#Insert
car_brands.insert(2, "Ford")
print(car_brands)

#Remove
car_brands.remove("Porsche")
print(car_brands)

if "Honda" in car_brands:
    print("Don't rice it.")
else:
    print("You are rich.")

car_brands = ["Ferrari", "Toyota", "Nissan", "Buggati", "Honda", "Lotus"]
car_manuf = list(car_brands)
print(car_manuf)

print("------------------")

#Tuple:
print("This is a tuple.")
science = ("Physics", "Chemistry", "Biology", "Mathematics", "Stat.") #It's Unchangeable/Immutable.
print(science)
print(science[1:3])
print(science[:-1])
print(science[-0:])
print(science[-3:-1])

for x in science:
    print(x)

#Trying to change it like list will result in an error.
#To modify it you need to convert it into a list first.

x = list(science)
x.remove("Stat.")
print(x)
x.append("Higher Maths")
print(x)

#Loop through a tuple:
for x in science:
    print(x)

#Item exists or not:
if "Mathematics" in science:
    print("We study it.")

#Tuple Length:
print("The length of this tuple is:")
print(len(science))

#Tuple w/ only one item:
x = ("Rice",)
print(type(x))
x = ("Rice")
print(type(x)) #NOT a tuple but a string

#Adding tuples:

commerce = ("Accounting", "Management", "Finance", "Banking")
z = science + commerce
print(z)

#Tuple Methods:

x = ("12", "10", "12", "24", "13", "16")
y = x.index("16")
print(y)
z = x.count("12")
print(z)

#Sets:
print("This is a set:")
rainbow = {"Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"}
print(rainbow) #Will be printed RANDOMLY, NOT IN ORDER

for x in rainbow:
    print(x)

if "Violet" in rainbow:
    print("It is a color of rainbow.")

#Adding items in set:
rainbow.add("White")
print(rainbow)

#Removing items in set:
rainbow.discard("Red") #remove method can also be used
print(rainbow)

rainbow.pop() #it'll remove a random item in a set
print(rainbow)

rainbow.clear() #clearing the set
print(rainbow)

#Adding multiple items:
some_colors = {"red", "green", "blue"}
some_colors.update(["black", "white"]) #curly brackets can also be used here
print(some_colors)

#Length:
print(len(rainbow))
print(len(some_colors))

print("------------------")

#Dictionary:

demo_dict = {
    "key1" : "element1",
    "key2" : "element2",
    "key3" : "element3"
}

print(demo_dict)

#Looping through the keys:
for x in demo_dict:
    print(x)

#Looping through the keys and elements using the items method:
for x,y in demo_dict.items():
    print(x,y)

print("------------------")

ford_gt_1967_mkII = {
    "Engine Displacement:" : "7.0L FE (427 ci)",
    "Gearbox:" : "Kar kraft 4-speed",
    "Major Victories:" : "Le Mans '66, Sebring '66",
    "Year:" : 1966
}

print(ford_gt_1967_mkII)

print("------------------")

x = ford_gt_1967_mkII.get("Gearbox:")
print("The Gearbox is:")
print(x)

print(len(ford_gt_1967_mkII))

ford_gt_1967_mkII["Movie appearence:"] = "Ford V Ferrari"
print(ford_gt_1967_mkII)

for x,y in ford_gt_1967_mkII.items():
    print(x,y)

print("------------------")

ford_gt_1967_mkII = {
    "Engine Displacement:" : "7.0L FE (427 ci)",
    "Gearbox:" : "Kar kraft 4-speed",
    "Major Victories:" : "Le Mans '66, Sebring '66",
    "Year:" : 1966
}

print("FORD GT MKII:")
for x in ford_gt_1967_mkII.values():
    print(x)

print("------------------")

ford_gt_1967_mkII["Year:"] = 1967
print(ford_gt_1967_mkII)

ford_gt_1967_mkII.pop("Year:")
print(ford_gt_1967_mkII)

x = ford_gt_1967_mkII.get("Engine Displacement:")
print(x)

print("------------------")

ford_gt_1967_mkII["Power:"] = "485bhp @ 6200rpm"
ford_gt_1967_mkII["Torque:"] = "475Nm @ 5000rpm"
ford_gt_1967_mkII["Power/Liter:"] = "69hp"
print(ford_gt_1967_mkII)

for x,y in ford_gt_1967_mkII.items():
    print(x,y)

if "Major Victories:" in ford_gt_1967_mkII:
    print("They comprehensively won those races.")

print("------------------")

x = input()