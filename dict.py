state = ['Maharashtra','Assam','Rajsthan','Goa','Gujrat']
capital = ['Mumbai','Dispur','Jaipur','Panji','Gujrat']
famous = ['Vada Pav','Tea','Bangls','Beach','Jalebi']

dt = dict(zip(state,famous))
print(dt)

for i, j in dt.items():
    print(f"{i[0:3]} {j[-3:]}")

t = { }
for i , j in dt.items():
    t.update({i[0:3]:j[-3: ]})
print(t)

for i in range(1,6):
    for j in range(1, i + 1):
        print("*", end =" ")
    print()

for i in range(5,0,-1):
    for j in range(1, i + 1):
        print("*", end =" ")
    print()

for i in range(1,6):
    for j in range(5 - i):
        print(" ", end ="")

    for k in range (1,i+1):
        print("*", end = " " )
    print()


n = int(input("Enter the how star you want in your pyramid: "))
for i in range(n):
    for j in range(n - i):
        print(" ", end ="")

    for k in range (1,i+1):
        print("*", end = " " )
    print()

n = int(input("Enter the how star you want in your pyramid: "))
for i in range(1, n):
    for j in range(n - i):
        print(" ", end ="")

    for k in range (1,i + 1):
        print("*", end = " " )

    print()

for i in range (n, 0, -1):
    for j in range (n - i):
        print(" ", end = "")

    for k in range (1,i + 1):
           print("*", end = " " )
           
    print()
   