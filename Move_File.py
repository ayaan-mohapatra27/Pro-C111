import os
import shutil
source="C:/Users/ayaan/Downloads"
destination="C:/Users/ayaan/OneDrive/Desktop/ProC111Files"
fileList= os.listdir(source)
length = len(fileList)
print(length)
#print(fileList)
for i in range(0, length):
    root,ext=os.path.splitext(fileList[i])
    print(root)
    print(ext)
    