# Continue keyword use for skiping values


# #simple program :
# i = 1
# while i <= 5 :
#     if( i == 3):
#         i += 1
#         continue
#     print(i)
#     i +=1
        

limt = int (input("Enter your limit : "))

x = int (input("Enter one num that you want to skip : "))

i = 1
while i <= limt :
    if( i == x):
        i += 1
        continue
    print(i)
    i +=1
        