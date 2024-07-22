import os

# to create a file
# os.system("touch osfile.txt")
# os.system("mkdir folder")

# os.rmdir("folder")
if os.path.exists("osfile.txt"):
    print("File exists")
    os.remove("osfile.txt")
else:
    print("File does not exist")
