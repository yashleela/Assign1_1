print( "first number")
first = input()
print ("second number")
second = input()
print ("third number")
third = input()
all = first == second and second == third and third == first
print ("All are equal:",all)
any = first == second or second == third or third == first
print("Any of three are equal:",any)