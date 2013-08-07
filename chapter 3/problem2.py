import os
import collections
extensions = collections.defaultdict(int)

for path, dirs, files in os.walk('/home/rainu/soln/chapter 2'):
   for filename in files:
       extensions[os.path.splitext(filename)[1].lower()] += 1

for key,value in extensions.items():
    print  key, ' ', value
