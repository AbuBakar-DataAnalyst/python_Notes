# Their are some Function that we can use directly by providing commond

statm = "Hello bro , How are you.where are going"

print(statm.endswith("ing")) # True or False
print(statm.endswith("bcd")) # True or False

# Capitalize do first index capital
print(statm.capitalize())

# Replace / like : where replace by bro
print(statm.replace("bro" , "where"))
 
# Find any word in string
print(statm.find("a")) # it will find First a
print(statm.find("How")) # or

# count that how many times word lies in this
print(statm.count("o"))
print(statm.count("bro")) # Or