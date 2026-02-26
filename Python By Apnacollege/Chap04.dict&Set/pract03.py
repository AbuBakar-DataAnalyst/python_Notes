# WAP to enter of 3 subjects from the user snd store them in a dictionary.start with empty
# dictionary & add one by one .Use subject name as key & marks as value

dict = {} # empty dict

x = int(input("Enter the PF marks : "))
dict.update({ "Programing Fundamentals : " : x})

x = int(input("Enter the AICT marks : "))
dict.update({ "Application of Information & Communication Technology : " : x})

x = int(input("Enter the FE marks : "))
dict.update({ "Functional English" : x})


print(dict) 