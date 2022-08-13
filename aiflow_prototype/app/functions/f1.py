
import os
import time

path = r"/opt/temp/fol1"

print("f1 started")
try:
    os.rmdir(path)
except:
    print("no folder")
time.sleep(20)
os.makedirs(path)
time.sleep(10)
print("f1 ended")
