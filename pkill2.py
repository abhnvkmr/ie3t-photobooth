import commands
import os
import time
f = open('kill.txt','w')
time.sleep(5)
status,output = commands.getstatusoutput("ps -e | grep feh")
output = output.lstrip()
temp = output.split(' ')
print(temp)
os.system("kill -9 " + temp[0])
f.write("kill -9 " + temp[0])
f.close()
