def gv(x):
	import os, time
	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(x)
	print "last modified: %s" % time.ctime(mtime)


gv('/home/rainu/soln/problem1.py')
