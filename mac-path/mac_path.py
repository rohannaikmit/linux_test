import os

while True:
    path=input("Please Enter mac-Os path : \n")
    
    for_back_slash=path.replace('/','\\')

    win_path=for_back_slash[34:]
    print("\\\isilon2%s" %win_path)
    for i in range(4):
        print("\n")

#smb://isilon2.pun.stereodstaff.com/jobpen/projects/mvfth/methodvancouver/from_stereod/20180608