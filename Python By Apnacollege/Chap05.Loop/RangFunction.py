# range function returns a sequence of numbers,starting from 0 by default & 
# increment by 1(by default),and stop befor a sepcified number
# range(start , stop , step)

# range(only one)
 
for i in range(5):
    print(i)

# range(two)
 
for i in range(1 , 5):
    print(i)    


# range(three)
 
for i in range(0 , 20 , 5):
    print(i)

# print 1 to 100    

for i in range(1 , 100):
    print(i)

# print 100 to 1  

for i in range(100 , 0 , -1):
    print(i)    


# print Table like 5 

n = int(input("Input number here : "))
for i in range(1 , 11):
    print(i*n)    