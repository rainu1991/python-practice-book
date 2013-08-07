import urllib2

def get_external_ip():
    ip = urllib2.urlopen(" http://httpbin.org/get").read()
    print ip



get_external_ip()
