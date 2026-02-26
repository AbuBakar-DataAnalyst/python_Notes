
str = input("Enter your Text : ")
vovel = "aeiou"
coutn = 0

for i in str.lower(): # it will handle the capital later to lower
    if( i in vovel):  #we use (in) instead of (==) bcause we check all num in list 
        coutn +=1     #(in) is reserved key word and

print ("Total vovels in this are : " , coutn)        
