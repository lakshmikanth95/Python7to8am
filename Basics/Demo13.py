def parrot_trouble(hour):
    if hour>=0 and hour<=23:
        if hour<7 or hour>20:
            return  True
        else:
            return False
    else:
        return False
res=parrot_trouble(5)
print(res)
