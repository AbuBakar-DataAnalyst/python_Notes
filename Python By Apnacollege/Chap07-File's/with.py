with open ( "inform.text" , "r" ) as f: # better syntex for file I/O.
    store = f.read()
    print(store) # it's not compulsory to close the file.outo closed by with suntex.