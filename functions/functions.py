# Hello World With Fun Fun Functions
def say_hello():
    print("Hello World!")
say_hello()

# add 2 numbers
def wish_me(name):
    print("Hey {name}! Hello")
wish_me("Teja")

def add_nums(num1, num2):
    return num1+num2
print("Sum of 2 numbers is: ",add_nums(4,5))

# Fun Game
def know_your_luck(int1:int, int2:int) -> bool:
    if int1==int2:
        return False
    elif ((int1 >= int2) and (int1%int2==0)):
        return True
    elif ((int1 <= int2) and (int2%int1==0)):
        return True
    else:
        return False
print("Let's have fun game")
int1 = int(input("Enter Num1 "))
int2 = int(input("Enter Num2 "))
if know_your_luck(int1,int2):
    print("Your are the Luckiest Person 🤩")
else:
    print("You are unlucky🥴")

# *args

def your_emojis(*args):
    print("Your fvrt emojis are ", args)

your_emojis("😀","😁","😂","🤣","😃","😄","😅","😆","😉","😊","😋","😎","😍","😘","🥰")

# nested functions
def outer():
    def inner():
        print("from inner")
    print("From Outer")
    return inner()

outer()
# First order Function
new_name = outer
new_name()

#closures
def outer():
    print("From Outer")
    def inner():
        print("from inner")
    return inner

outer()()

# Lambda Function
square_of_num = lambda x:x*x
print(square_of_num(20))