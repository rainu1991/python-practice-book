N=10
f=open("/home/rainu/soln/chapter2/she.txt")
for i in range(N):
    line=f.next().strip()
    print line
f.close()
