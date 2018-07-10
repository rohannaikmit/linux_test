import random

bc_list=['Rohan','Mukesh','Vinay','Shital','Shital1','Dnyaneshware','Dnyaneshware1','Amol','Pankaj','Hari']

bc_name=random.randint(0,9)

lucky_name=bc_list[bc_name]

#print lucky_name

with open("bc_LastNames.txt",'r+') as fh:
    a=fh.read()
    #print a
    lst=a.split(",")
    for i in lst:
        print i
        if i[:-1]==lucky_name or i== "":
            print "Name repeated Spinn one more time"
        else:
            print lucky_name
            break
    fh.write(lucky_name+',')
  
  