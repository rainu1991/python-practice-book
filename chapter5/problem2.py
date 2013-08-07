def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def printlines(lines):
    n = 40	
    for line in lines:
	if len(line) > 40:	
           print line

def main(filenames):
    lines = readfiles(filenames)
    printlines(lines)
