# Write  a recursive function to print all elements in a list
# Hint : use list & index as parameter

city = ["islamabad" , "karachi" , "lahore" , "rawalpindi" , "mianwali"]

def count(list , index):
    if ( index == len(list)):
        return
    print(list[index])
    count(list , index+1)

count(city , 0)    