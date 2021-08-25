x = 0
while x<10:
    print("square of ",x," is " ,x*x)
    x+=1


lst = ["Aagam", "Baa", "Uday"]
i = 0
while i<len(lst):
    print(lst[i])
    i+=1
for name in lst:
    print(name)

j=0
while j<len(lst):
    if lst[j] == "Uday":
        print("Maa Baa puli🐯")
        break
    j+=1
else:
    print("Maa baa pilli")

for item in lst:
    if item == "Uday":
        print("We find that Ninja🐱‍👤")
        break
else:
    print("Not found")

st = "Teja003"
for i in st:
    if i == '0':
        print("Escape")
        break
    print(i)

