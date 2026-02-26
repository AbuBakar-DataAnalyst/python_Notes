# Multiplication Table printer 
# print the tabl up to 10 , but skip the 5 itration

n = int(input("Input table : "))
end = int(input("Input your ending point : "))

i = 1
while i <= end:
    if( i== 5 ):
        continue  # this key wor will skip the number that you want
    print( n, "x" , i , "=" , i*n )
    i += 1   