with open ('/home/rainu/soln/z.py') as fi, open('/home/rainu/soln/v.txt', 'w') as fo:
    fo.write('\n'.join(reversed(fi.read().splitlines())))
