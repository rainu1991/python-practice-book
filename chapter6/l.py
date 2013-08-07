import os
import sys
def write_files(files):
    for element in os.listdir(files):
        if os.path.isdir(element):
            print('*' + element)
            write_files(element)
        else:
            print('-' + element)


write_files('/home/rainu/soln')
