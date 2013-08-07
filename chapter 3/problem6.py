import sys
import urllib
def main():
    # print command line arguments
    for arg in sys.argv[1:]:
       response = urllib.urlopen(arg)
       print response.headers

if __name__ == "__main__":
    main()
