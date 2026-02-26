f = open( "other.text" , "r+" ) # for appending use (a+) intead of r+
                                 # (+) is use for both operation like reading & writing.
f.write("abc")
print(f.read())
f.close()

