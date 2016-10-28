#!/usr/bin/python

import csv

ifile  = open('3.csv', "rb")
text_file = open("Output.txt", "w")
reader = csv.reader(ifile)
text_file.write('}\n')
rownum = 0
for row in reader:
    # Save header row.
    colnum = 3
    count=0

    for col in row:
        if count==3:
            #print '{%s}\n' % (col)
            text_file.write("{%s}\n" % col)
        #colnum += 1
        count+=1
        #print '-----------------------------'    
    rownum += 1
text_file.write('{')
ifile.close()
text_file.close()