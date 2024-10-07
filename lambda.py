##LAMBDA FUNCTION
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expressio

##Syntax
#lambda arguments : expression
x = lambda a: a * 5
print(x(10))
y = lambda num1,num2: num1 + num2
print(y(1,3))
def multFunction(num):
    return lambda a: a * num
myDoubler = multFunction(2)
myTrippler = multFunction(3)
print(myDoubler(11), myTrippler(11))