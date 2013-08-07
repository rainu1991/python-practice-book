import os
x = []
count = 0
os.chdir("/home/rainu/soln/chapter5")
for files in os.listdir("."):
    if files.endswith(".py"):
        x.append(files)
for f in x:
        for line in open(f):
            count = count + 1
print count
