#028)	Python Program to Find LCM

def calc_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while True:
        if (greater%x==0) and (greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm

n1= int(input("Enter number 1:"))
n2= int(input("Enter number 2:"))
print(f"The L.C.M of {n1} and {n2} is",calc_lcm(n1,n2))
