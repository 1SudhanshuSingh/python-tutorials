##LOGICAL CONDITIONS
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#IF STATEMENT
a = 10
b = 20
c = 30
if(a < b):
    print(f"a is less than b as {a} is less than {b}")
#ELIF
if(a < b):
    print(f"a is less than b as {a} is less than {b}")
elif(a > b):
    print(f"a is greater than b as {a} is greater than {b}")
#ELSE
if(a < b):
    print(f"a is less than b as {a} is less than {b}")
elif(a > b):
    print(f"a is greater than b as {a} is greater than {b}")
else:
    print("a and b are equal")
##Shorthand if statement
if(a < b) : print("a is less than b")
##Shorthand if else statement (Ternary Operators, or Conditional Expressions)
print("b is greater than a") if (b > a) else print("b is greater than a")
## and, or, not logical operators
if(a > b and a > c): print("a is bigger") ##in and both conditions has be true
if(a > b or a > c): print("a may be bigger") ##in or any one conditions has be true
if(a != 10): ##not is !, it opposites the condition as not equals, !False(becomes true), !True becomes(false)
    print("a is not 10")
else:
    print("a is 10")
##nested ifs
a = 15
if(a > 10):
    if(a < 20):
        print("a is between 10 and 20")
##pass statement - if statements cant be empty, we can use pass to avoid the error if empty if statement
x = 13
y = 22

if x > y:
  pass

