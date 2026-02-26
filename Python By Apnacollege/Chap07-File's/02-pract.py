# waf that replace all occurence of "java" with "python" in above file que#01.

with open(  "practice.text" , "r" ) as f: # we can use other word instead of (f)
 
    data = f.read()

new_data = data.replace( "java" , "python" )
print(new_data)    