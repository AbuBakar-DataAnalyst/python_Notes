

dict = {
"name" : "Abu Bakar Siddique" ,
"Roll number" : 567 ,
"cgpa" : 7.78 ,
"pass" : True,
"subjects" : ["ICP" , "OOP" , "DLD"] # we can use list [] & Tuples () in dictionary
}
print(dict)

print(dict.keys()) # .keys() / it return all keys mein first values.

print(dict.values()) # .values() / it return all keys mein 2nd values.

print(dict.items()) # .items() / it return both kess & values mean pairas tuple. 

print(dict.get("name")) # .get() / it return all keys mein first values.
 # print (dict["name"]) / this method is pefect as compaired to direct calling keys
                         # bacause it cant generat errors  

print(dict.update({ " section" : "A"}))                          