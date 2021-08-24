is_rainy = True
too_rainy = False
# if
if(is_rainy):
    print("Take Umbrella☂")

# if-else
if(not is_rainy):
    print("Take Umbrella☂")
else:
    print("No need of umbrella🌂")

# if-elif-else
if(not is_rainy):
    print("It's rainy")
elif(is_sunny:=True): # Walrus Operator
    print("It's sunny")
else:
    print("It's not rainy & sunny")

# Nested if-else
if(not is_rainy):
    if(too_rainy):
        print("It's too rainy⛈")
    else:
        print("Moderate rain☔")
elif(is_sunny):
    if(too_sunny:=False):
        print("Not Sunny")
    else:
        print("it's Hot🥵")
else:
    print("Good Weather😎")    
