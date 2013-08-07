def is_list(p): 
return isinstance(p, list)

def deep_reverse(mylist):
result = []
for e in mylist:
    if isinstance(e, list):
        result.append(deep_reverse(e))
    else:
        result.append(e)
result.reverse()
return result

