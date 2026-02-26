# Their are many bulit in Methods in python that we can use directly

# 01 (.append)/ it will add one word or statment element at the end
app = [1 , 2 , 3]
app.append(4) # .append("Koch bhi") its also posible
print (app)

# 02 (.sotr) it arrang the values / Ascending orer

arr = [6,4,3,2,1,5,7] # we can also write here string like [ "z" , "who" , "Thye" , "a" , "c"]
arr.sort()            # it will arrang them by first elemnt according to alphabets manner
print(arr)            # Answr ["a", "c" , "thye" "who" , "z"] 

# 03 .sotr(reverse=True) it will reverce the list / Descending order

arr = [6,4,3,2,1,5,7]
arr.sort(reverse=True) # First arrange then reverce
print(arr)  

# 04 .reverce() / it will reverce the values without arranging

arr = [6,4,3,2,1,5,7]
arr.reverse()
print(arr) 

# 05 .insert(wants indux , replace word) & the word also come that you replace indux

arr = [1,2,3,4]
arr.insert(2 , 5) # its mean u r replacing value of 2indux with 5.
print(arr) 

# 06 .remove(type number or string) / it will remove that will come first

arr = [1,2,3,4.6,3,6,3]
arr.remove(3)
print(arr) 

# 07 .pop(indux) / remove element at this indux

arr = [19,289,378]
arr.pop(2)
print(arr) 

