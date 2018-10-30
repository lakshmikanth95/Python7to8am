
no=1
for x in range(1,5):
    for y in range(x):
        print(no,end=" ")
        no+=1
        if no==10:
            no=0
    print()

print("--------------------")

no = 5
for x in range(1,6):
    for y in range(x):
       if x == 4 and y == 2:
           print(40,end=" ")
       else:
           print(no,end=" ")
           no+=5
    print()


