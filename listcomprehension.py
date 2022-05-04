#templist=[expression loop condition]
tmp=[i for i in range(1,20) if i%2==0]
print (tmp)

mystr="ABHISEK"
tmpstr=[i for i  in mystr]
print(tmpstr)

line="This is Python Class"
tmplist=line.split()
words=[w for w in tmplist if w!="is"]
print(words)

strjoin="#".join(tmplist)
print(strjoin)

i=len(line)
print (i)
