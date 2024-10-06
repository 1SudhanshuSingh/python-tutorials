##DATATYPES
## Text Type:	str
## Numeric Types:	int, float, complex
## Sequence Types:	list, tuple, range
## Mapping Type:	dict
## Set Types:	set, frozenset
## Boolean Type:	bool
## Binary Types:	bytes, bytearray, memoryview
## None Type:	NoneType

##NUMBERS
x = 1 ##int
y = 1.5 ##float
z = 1j ##complex j is imaginary part
print(type(x))
print(type(y))
print(type(z))
##type conversion using python functions int(), float(), and complex()
a = int(y)
b = complex(x)
print(type(a))
print(type(b))
##casting it is called type conversion
##casting string type to a numner
a = 1
b = str(a)
print(a == b) ##false as '1' is not equal to 1

##STRINGS
a = "My name is sudhanshu and i am a full stack developer"
##slicing a string
print(a[11:20]) ##[start point:end point]
##modify strings
uppercaseText = a.upper()
print(uppercaseText) ##uppercase
print(uppercaseText.lower()) ##lowercase
b = "    Hello There!   "
print(b.strip()) ## removes whitespaces from begining and end
replacedWord = b.replace("H", "Z") ##replaces letter H to Z
print(replacedWord)
print(a.split()) ## splits everyword as an item of array or list ['My', 'name', 'is', 'sudhanshu'...]
##concatenate strings or join strings
greeting = "namaste"
person = "sudhanshu"
print(greeting + " " + person)
##format string - use any variable into string right away by just adding f
age = 31
print(f"I am {age} years old")
##escape characters
##\'	Single Quote	
##\\	Backslash	
##\n	New Line	
##\r	Carriage Return	
##\t	Tab	
##\b	Backspace	
##\f	Form Feed	
##\ooo	Octal value	
##\xhh	Hex value
text = "We are proud to be the \"Developers\" of India" ##\" to escape ""

##BOOLEAN means true or false
isSmart = True
if isSmart:
    print("I am smart")
##casting with bool() any datatype will always be true except None
print(bool(3.14))
print(bool("Hello"))
print(bool(None))

##LIST OR ARRAY
sports = ["cricket", "football", "tennis", "basketball"]
##list can store different values of different datatypes as well 
myAttributes = ["Sudhanshu", 31, True]
##access list items by index number
print(sports[0]) ##first item will always have index 0
print(sports[-1]) ##print item from the end
##ranges of indexes
print(sports[1:3]) ## get item from index 2 to 5
print(sports[1:]) ## all items after index 1 (not including 1)
print(sports[:2]) ## all items before index 2 (not including 2)
##check if item exist
if "cricket" in sports:
    print("Cricket Fan")
##change list item
sports[0] = "Kabaddi" ## with index
print(sports)
sports[1:3] = ["Badminton", "Hockey"]
print(sports)
##insert item based on index
sports.insert(2, "Taekwondo")
print(sports)
##adding items using append and extend
sports.append("Wrestiling") ##apends to item to the end of array
print(sports)
newSportsList = ["Swimming", "Baseball", "E-sports"]
sports.extend(newSportsList)
print(sports)
##remove items from list using remove, pop, delete, clear
sports.remove("Baseball") ##removed the specified item
print(sports)
sports.pop() ##removes last item in list
print(sports)
removedItem = sports.pop(3) ##removes 3 indexed item in list
print(sports) ##can store removed item in a variable
print(removedItem) 
del sports[0] ##deletes indexed item and cant store in variable
print(sports)
#sports.clear() ## clears the list but does not delete the variable of list completely
#del sports ##deletes whole list
##LOOPS
##for loop
for sport in sports:
    print(f"i love {sport}")
for number in range(10): ##range gives us range between 0 and 10 here
    print(number)
for i in range(len(sports)):
    print(f"{i + 1} : {sports[i]}") ## print based on index number
##shortcut approach for doing above using enumerate
for index, sport in enumerate(sports):
    print(f"{index + 1} : {sports[i]}") 
##while loop
j = 0
while j < len(sports):
    print(f"i love {sport}")
    j+=1 ##j = j+1
##list comprehension - shorted syntax if want to create new list based on values of existing list
fruits = ["watermellon","apple", "kiwi", "banana", "mango", "cherry", "gauva"]
fruitsWithLetterO = []
for fruit in fruits:
    if "o" in fruit:
        fruitsWithLetterO.append(fruit)
print(fruitsWithLetterO)
##using list comprehension
fruitsWithOComp = [fruit for fruit in fruits if "o" in fruit] ##fruitsWithOComp = [expression for item in iterable if condition == True]
print(fruitsWithOComp)
##more example of using list comprehension
evenOddCheck = ["Even" if number %2 == 0 else "Odd" for number in range(100)] ## expression is even if else condition for item is number in iterable is list/range
print(evenOddCheck)
##SORTING
fruits.sort() ##sort alphabatically and reassign the value to the original array/list
print(fruits)
##sorting reverse
fruits.sort(reverse=True)
print(fruits)
##OR
fruits.reverse()
print(fruits)
##copy list/array using copy method and list method and slice operator
fruitCopy1 = fruits.copy()
fruitCopy2 = list(fruits)
fruitCopy3 = fruits[:]
print(fruitCopy1, fruitCopy2, fruitCopy3)
##Join lists/array using join +, append method and exten method
combinedSportsAndFruits1 = sports + fruits
print(combinedSportsAndFruits1)
##append method
for fruit in fruits: ##append single item of array/list to the existing array at the end
    sports.append(fruit)
print(sports)
##extend method
sports.extend(fruits) ##does not return new array/list, do changes in existing array/list
print(sports)
##LIST METHODS LIST
##append()	Adds an element at the end of the list
##clear()	Removes all the elements from the list
##copy()	Returns a copy of the list
##count()	Returns the number of elements with the specified value
##extend()	Add the elements of a list (or any iterable), to the end of the current list
##index()	Returns the index of the first element with the specified value
##insert()	Adds an element at the specified position
##pop()	Removes the element at the specified position
##remove()	Removes the item with the specified value
##reverse()	Reverses the order of the list
##sort()	Sorts the list

##TUPLES - A tuple is a collection which is ordered and unchangeable
tupleFruit = ('apple', 'banana', 'orange')
print(tupleFruit)
# Tuple items are ordered, unchangeable, and allow duplicate values
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Since tuples are indexed, they can have items with the same value:
# All same as list/array (access, update, unpack, loop, join)

##SETS
##A set is a collection which is unordered, unchangeable*, and unindexed (it will give unique values, if repeated items are there it will pick only one)
fruitsSet = {"apple", "banana", "banana", "banana", "banana", "orange", 1, True, 4.2, False, 0} ##False and 0 are considered the same value in sets, and are treated as duplicates
print(fruitsSet)
##Cannot access items in a set by referring to an index or a key
for fr in fruitsSet:
    print(fr)
##to check if item is present
print("orange" in fruitsSet)
print("avacado" not in fruitsSet)
##adding set item
fruitsSet.add("grapes")
print(fruitsSet)
##to add 2 sets or any iterable use update method on set
vegetableSet = {"potato", "tomato", "cauliflower"}
cerealList = ["oat", "wheat", "rice"]
fruitsSet.update(vegetableSet)
fruitsSet.update(cerealList) ##result will be the Set
print(fruitsSet)
##remove item using remove(), or the discard(), pop(), clear() del
fruitsSet.remove("grapes") ##remove will throw error if the given item not found
print(fruitsSet)
fruitsSet.discard("rice") ##discard will not throw error if the given item not found
print(fruitsSet)
fruitsSet.clear() ##clear will clear the items and return empty Set
print(fruitsSet)
del fruitsSet ##delete fruitsSet variable
##looping will be same as other iterables using for loop
##to join sets we use union() ( | ) and update() ( |= )
set1 = {"a", "b","c"}
set2 = {1,2,3}
unionedSet = set1.union(set2)
print(unionedSet)
##to keep only duplicates between Sets use intersection()
nameSet1 = {"aman", "rohit", "madan", "yash"}
nameSet2 = {"aman", "rohit", "achint", "shubh" }
intersectionSet = nameSet1.intersection(nameSet2)
print(intersectionSet)
##to keep the item from first set which are not in second set use difference()
differSet = nameSet1.difference(nameSet2)
print(differSet)
##symmetric_difference() (^) ymmetric_difference()_update (^=) method keeps all items EXCEPT the duplicates.
symmDiffSet = nameSet1.symmetric_difference(nameSet2)
print(symmDiffSet)

##PYTHON DICTIONARIES (OBJECTS)
car = {
    "id": 1,
    "brand": "tata",
    "model": "safari",
    "year" : 2022
}
print(car)
##access items in dictionaries / objects
print(car["model"])
##change dictionary / objects items
car["model"] = "nexon"
print(car)
car.update({"year" : 2024})
print(car)
##adding itmes to dictionary / objects
car["color"] = "black"
print(car)
car.update({ "price": 2400000 })
print(car)
##remove items using pop(), popitem(), clear(), del
car.pop("model")
print(car)
popepdItem = car.popitem()
print(car, popepdItem)
##clear and del is same as above, del deletes variable where clear empties the dictionary / object
##looping through dictionary / object
for c in car: ##it will print all the keys
    print(c)
for c in car: ##it will print all values
    print(car[c])
for c in car.keys(): ##it will print all the keys
    print(c)
for c in car.values(): ##it will print all values
    print(c)
for key,val in car.items(): ##it will print both key and val
    print(key,val)
##copy dictionary / object using copy()
car2 = car.copy()
##copying using built in dict
car3 = dict(car)
print(car3, car2)
##nested dictionary / object
myfamily = {
  "child1" : {
    "name" : "Aradhana",
    "year" : 1984
  },
  "child2" : {
    "name" : "Himanshu",
    "year" : 1985
  },
  "child3" : {
    "name" : "Sudhanshu",
    "year" : 1993
  }
}
##accessing nested dictionary / object
print(myfamily["child1"]["name"])
##looping through nested dictionary / object
for x, obj in myfamily.items():
    for y, innerObj in obj.items():
        print(f"{x} => {y} : {innerObj}")