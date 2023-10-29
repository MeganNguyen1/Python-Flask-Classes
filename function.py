# Function is a template to organise is the code and make it reusable

# This is function definition and a,b are the parameters
# def add(a,b):
#     sum = a + b 
#     print(sum)

# this is function call, function will not excute without calling it
# add(13,8)

# we make the function once and call it for different values

# def divide(a,b):
    # quotient = a/b 
    # print(quotient)
# 
# divide(245,7)
# 
# def mulitply(a,b):
    # product = a*b 
    # print(product)
# 
# mulitply(45,9)

def greater(a,b):
    if a > b:
        print("a is greater")
    else:
        print("b is greater")

greater(42,902)
    
def greatest(a,b,c):
    if a > b and a > c:
        print("a is the greatest")
    elif b > a and b > c:
        print("b is the greatest")
    else:
        print("c is the greatest")

greatest(102, 307, 457)

def information(name, age, place):
    print(f"{name} is {age} years old and lives in {place}")

information("Andy", 12, "Texas")
