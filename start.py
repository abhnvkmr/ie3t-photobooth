import os
execfile('capture.py')
f = open('send1.txt','w') 
ans = raw_input("PAID[Y/N] : ")
if ans=='y' or ans=='Y':
    mail = raw_input("Enter Email[Seperated by comma] : ")
    mail = mail.split(',')
    for i in range(len(mail)):
        f.write(mail[i])
    try:
        print("WORKING")
        execfile('mail.py')
    except:
        print("Error")
elif ans=='n' or ans=='N':
    try:
        print("WORKING")
        execfile('wmrk.py')
        execfile('mail.py')
    except:
        print("Error")

    

    
    