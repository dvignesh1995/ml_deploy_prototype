
import os
import time

path = r"/opt/temp/fol3"

print("f3 started")
try:
    os.rmdir(path)
except:
    print("no folder")
time.sleep(10)
os.makedirs(path)
time.sleep(10)
print("f3 ended")
