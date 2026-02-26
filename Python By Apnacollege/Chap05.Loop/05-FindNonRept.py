# Finf the first non repeative character

str = input("Enter the String : ")

for char in str:
    if ( str.count(char) == 1 ):
        print ("The charecter is : " , char )
        break