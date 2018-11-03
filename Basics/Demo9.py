name=input("employee name:")
salary=float(input("employee salary:"))
designation=input("enter designation:")
bonus=0
if designation=="analyst":
    bonus=10*(salary/100)
    salary=salary+bonus
    print(salary)
elif designation=="manager":
    bonus=20*(salary/100)
    salary=salary+bonus
    print(salary)
elif designation=="clerk":
    bonus=5*(salary/100)
    salary=salary+bonus
    print(salary)
else:
    print("invalid designation")