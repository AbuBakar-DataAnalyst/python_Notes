# Search the from Tuple using loop
# (1, 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)

tpl = (1, 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)

x = 36 # we want to Search this number

i = 0
while i < len(tpl):
    if(tpl[i] == x):
        print("Founded at index : " , i)
        break 
    i += 1
