name=input("customer name:")
slab=input("slab type:")
units=float(input("units"))

if slab=="industry":
    bill=units*5.25
    print(bill)
elif slab=="commercial":
    bill=units*4.00
    print(bill)
elif slab=="residence":
    bill=units*3.08
    print(bill)
else:
    print("invalid slab type")