new_list=[["B",12],["C",2],["V",7],["E",27],["Q",45],["L",17]]
#def fn(x):
#    return x[1]
#new_list.sort(key=fn)
#print(new_list[1])
m=sorted(new_list,key=lambda x:x[1])
print(m[1][0])
