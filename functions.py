##Functions
def greeting():
    print("Greeting to you")
greeting()

##Parameters and Arguments
def printname(fname, lname):
    print(f"{fname} {lname}")
printname("Sudhanshu", "Singh")
##number of arguments is unknown use *(Arbitrary Arguments, *args)
def printAge(*age):
    print(age[2])
printAge(1,2,3,4,5)
##Keyword arguments (we can also send arguments with the key = value syntax)
def getPrice(p1, p2, p3):
    print(f"Total is {p1 + p2 + p3}")
getPrice(p1 = 5, p2 = 10, p3 = 15)
##Arbitrary keyword arguments
def getCar(**args):
    print(args["model"])
getCar(brand = "tata", model = "nano")
##Passing list as argument
def myGadets(gadgetArr):
    for g in gadgetArr:
        print(f"i like {g}")
myGadets(["xbox", "ps5", "macbook", "iPhone"])
##Return Values
def addNumbers(num1, num2):
    return num1 + num2
print(addNumbers(1,9))
##Default parameter value
def myFavCountry(country = "India"):
    print(country)
myFavCountry()
##pass statement
def passingFunction():
  pass
##positional only argument
def printEvenNum(x, /):
    print(x)
# printEvenNum(x=3) ##this will trow error
##Recursion (a defined function can call itself)
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(3)