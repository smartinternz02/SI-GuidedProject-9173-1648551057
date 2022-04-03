#Question: 1st
#Pogram:
print(7**4)
#Output: 2401

#Question: 2nd
#Pogram:
s="Hi there Sam!"
l=s.split()
l[-1]="dad!"
print(l)
#Output: ['Hi','there','dad!']

#Question: 3rd
#Pogram:
planet="Earth"
diameter=12742
print("The diameter of {} is {} kilometers.".format(planet,diameter))
#Output: The diameter of Earth is 12742 kilometers.

#Question: 4th
#Pogram:
lst=[1,2,[3,4],[5,[100,200,["hello"]],23,11],1,7]
print(lst[3][1][2][0])
#Output: 'hello'

#Question: 5th
#Pogram:
d={'k1':[1,2,3,{'tricky':['oh', 'man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])
#Output: 'hello'

#Question: 6th
#Answer:
print("Tuples and Lists are mutable but the values can't be alttered within an Tuple, it is possible in Lists")
#Output: Tuples and Lists are mutable but the values can't be alttered within an Tuple, it is possible in Lists

#Question: 7th
#Program:
def domain(a):
    return a.split("@")[-1]
print(domain("user@domain.com"))
#Output: domain.com

#Question: 8th
#Program:
def fun(a):
    return True if "dog" in a else False
print(fun("dog"))
#Output: True

#Question: 9th
#Program:
def fun(a):
    return a.count("dog")
print(fun("dot"))
#Output: 0

#Question: 10th
#Program:
def ticket(speed,bod):
    if bod:
        speed-=5
    if speed>80:
        return "Big Ticket"
    elif speed>60:
        return "Small Ticket"
    else:
        return "No Ticket"
#Output:
#print(ticket(65,False)) =>  Small Ticket
#print(ticket(86,True)) =>  Big Ticket
