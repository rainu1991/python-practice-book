with open('/home/rainu/soln/chapter2/she.txt', 'r') as rfp:
  with open('/home/rainu/soln/chapter2/b.txt', 'w') as wfp:
    for line in rfp:
      ilikethis = 'shells'	
      if ilikethis(line):
        wfp.write(line)
