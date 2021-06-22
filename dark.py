# -*- coding: utf-8 -*-
import os ,time
bannar = '''\033[94m
    ____             __  
   / __ \____ ______/ /__
  / / / / __ `/ ___/ //_/
 / /_/ / /_/ / /  / ,<   
/_____/\__,_/_/  /_/|_|  
'''

banner2 = '''\033[95m
         _   __                 __  
        / | / /___ __________  / /__
       /  |/ / __ `/ ___/ __ \/ //_/
      / /|  / /_/ / /  / /_/ / ,<   
     /_/ |_/\__, /_/   \____/_/|_|  
           /____/                   

                 \033[96m  [Created By Team Dark Hunter 141]



            \033[92mUsing Ngrok Without Mobile Hotspot

'''

os.system ('clear')
print bannar
print banner2
print ('\033[96m [✓] Downloading Ngrok File.......')

time.sleep (2)
print ''
os.system ('unzip Dark-Ngrok.zip')
os.system ('chmod 777 ngrok')
os.system ('cp ngrok $PREFIX/bin/')
print '\033[92m [✓] Ngrok Setup Done '
print ''
print ('\033[93m [$] Restart your termux and type [\033[91mEX : ngrok http 8080\033[93m]: ngrok ......')
print ''
os.system ('exit')
