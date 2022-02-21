import os , math , time
from sys import argv
import subprocess
unique=[]
dirs= argv[1]


try:
   n= int(argv[2])
   x=n
except:
   n=0
   x=n
   pass

while True:
    dirfiles = os.listdir(dirs)
    
    for qqq in  dirfiles:
       if qqq not in unique and os.stat(dirs+'/'+qqq).st_size > 108650979000:
           n+=1
           time.sleep(5)
           print('запускаю транс  ' + qqq + 'На джисоне номер :' + str(n))
           os.system(f'screen -dmS trans{n} rclone move {dirs}/{qqq} aws32: --drive-stop-on-upload-limit --transfers 1 -P --drive-service-account-file "/root/AutoRclone/accounts/{n}.json" -v --log-file /root/rclone1.log;')
           unique.append(qqq)
           
    time.sleep(30)
    if n == x+50:
        n=x 
