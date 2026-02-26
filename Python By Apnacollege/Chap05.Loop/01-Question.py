# count positive number 
# Given a list of numbers , count how many are positive.
# nembers = [ 1 , -2 , 3 , -4 , 5 , 6 , -7 , -8 , 9 , 10 ]

nembers = [ 1 , -2 , 3 , -4 , 5 , 6 , -7 , -8 , 9 , 10 ]
count = 0

for i in nembers:
    if ( i > 0):
        count += 1
print("The positve Total numbers are : " , count )        