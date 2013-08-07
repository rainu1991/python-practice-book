import sys
import urllib
def main():
    # print command line arguments
    for arg in sys.argv[1:]:
       mylines = urllib.urlopen(arg).readlines() 
    for item in mylines: 
	if "http://" in item: 
		print item[item.index("http://"):]
	
if __name__ == "__main__":
    main()	
