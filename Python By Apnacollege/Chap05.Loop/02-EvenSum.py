

# Sum of even numbers 
# calculate the sum of even numbers up to a given numbers n.

n = int(input("input your starting point : "))
end = int(input("input your ending point : "))

sum = 0
i = n
while i <= end: 
    if ( i%2 == 0):
      sum += i
    i += 1

print("The sum of this is : " , sum )    

# #for loop

# n = int (input ("Enter a numbr : "))
# sum = 0

# for i in range(1, n+1):
#     if( i%2 == 0 ):
#         sum += i
# print ("The sum of Even No in this list is : " , sum )        

