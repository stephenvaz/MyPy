def rewr():
    global sno, mname
    f = open("D:\\Users\Stephen\Dev\Git\Python\\text.txt","r")
    content = f.readlines()
    s = 0
    m = 1
    while s<13  :
        
        
        sno = content[s]
        print (sno)
        mname = content[m]
        print (mname)
        s = s + 2
        m = m + 2
        
rewr()


    