# Dictionary in python store data values in Key : values pair
# Thy are Unordered (random ayein gy Sequence sy ni aein gy),
# Mutable (changeable) & dont allow duplicate value
# you can store in dictionary String , floating & integer value

dict = {
"name" : "Abu Bakar Siddique" ,
"Roll number" : 567 ,
"cgpa" : 7.78 ,
"pass" : True,
"subjects" : ["ICP" , "OOP" , "DLD"] # we can use list [] & Tuples () in dictionary
}
print(dict)

# we can print any sapacific value (key)
print(dict["name"])
print(dict["cgpa"])