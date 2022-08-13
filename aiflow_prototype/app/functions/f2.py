
import os
import time

path = r"/opt/temp/fol2"

print("f2 started")
try:
    os.rmdir(path)
except:
    print("no folder")
time.sleep(10)
os.makedirs(path)
time.sleep(10)
print("f2 ended")
