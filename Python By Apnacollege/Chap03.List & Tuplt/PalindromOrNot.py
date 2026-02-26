# WAP to check if a list contains a palindrome of elements.(Hint : use copy()method) .
# (palindrome)/ Ham sedha likhein ya ulta but wo change na ho
# Exam : [1,2,3,2,1] other [1 , "abc" , "abc" , 1] 

check = [ 1 , 2 , 3 , 2 , 1 ]

copyofcheck = check.copy()
copyofcheck.reverse()

if (check == copyofcheck):
    print("Palindrom :")

else:
     print("Not Palindrom :")

# Second Program         

check2 = [1 , "abc" , "abc" , 2 , "yaho"] 
copy = check2.copy()
copy.reverse()
if (check2 == copy):
    print("Palindrom :")

else:
     print("Not Palindrom :")


# input leni ho to:


# list = []
# n = int(input("Kitne numbers enter karne hain? "))

# for i in range(n):
#     num = int(input("Number enter karo: "))
#     list.append(num)


