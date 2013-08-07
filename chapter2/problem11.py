 def dup(list_a):
  lis = []
  for i in range(len(list_a)):
   for j in range(i + 1, len(list_a)):
     if list_a[i] == list_a[j]:
      lis.append(list_a[i])
  print lis
 

