"""
Print integers 1 to N, but print “Fizz” if an integer is divisible by 3,
“Buzz” if an integer is divisible by 5,
and “FizzBuzz” if an integer is divisible by both 3 and 5
"""

num = int(input("Enter Your Number: "))
for i in range(num+1):
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
        continue
    if i%3==0:
        print("Fizz")
        continue
    if i%5==0:
        print("Buzz")
        continue
    else:
        print(i)