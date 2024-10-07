##WHILE LOOPS (executes a set of statements as long as a condition is true)
x = 10
# while x > 0:
#     print(x)
#     x-=1
##WHILE LOOP WITH BREAK
##With the break statement we can stop the loop even if the while condition is true:
# while x > 0:
#     print(x)
#     if x == 3:
#         break
#     x -= 1
##With the continue statement we can stop the current iteration, and continue with the next
while x > 0:
    x -= 1
    if x == 2:
        continue
    print(x)
##FOR LOOPS (for loop is used for iterating over a sequence)
##for loop in array / list
fruits = ["banana", "apple", "kiwi", "orange"]
for fruit in fruits:
    print(fruit)
strings = "omlettedufermarge"
# for letter in strings:
#     print(letter)
##continue and break
for letter in strings:
    print(letter)
    if letter == "m":
        break
for letter in strings:
    if letter == "m":
        print(letter)
        continue



