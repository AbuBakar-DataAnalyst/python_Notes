# find the fectorial usin loop

num = int (input("Enter a number : ")) 
fact = 1

for i in range( 1 , num+1): # Jab hamry pass starting ya ending point na ho to ham 
        fact *= i           # range() ko use krty hain

print("The Fecorial of" , num , "is" , fact)