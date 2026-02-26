# creat a file "practice.text" usin python .Add the following data in it.
# Hi everyone
# we are learning file I/O
# usin java

with open ("practice.text" , "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning file I/O\n") # for next line (\n)
    f.write("usin java\n")