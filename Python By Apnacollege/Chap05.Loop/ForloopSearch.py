# Search the number from Tuple using loop
# (1, 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)

tpl = (1, 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)

x = 36 # we want to Search this number

for elmt in tpl:
    if( elmt == x):
        print("Founded : " , elmt )
        break
    elmt += 1    