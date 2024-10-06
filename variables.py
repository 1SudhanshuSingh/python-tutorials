##VARIABLES
##declare and define variables at the same time
##not have to define data type of variable sepratly, python define datatype on its own when value passed
x = 3
name = "Sudhanshu"
##variable names best practise
##do not start with number or special character also do not use - in between words
firstName = "Sudhanshu" ##Camel case
last_name = "Singh" ## Snake case
MiddleName = "NA" ## Kebap case
##assign multiple values
num1, num2, num3 = 1,2,3
##unpacking variables from list (array)
a,b,c = [4,5,6]
##outputting variables
print (a,b,c)
##global vs local variable eg. with use of function
about = "cool" ##global scopped variable
def printAbout():
    about = "hot" ##local scopped variable
    print(about)
printAbout()
print(about)
