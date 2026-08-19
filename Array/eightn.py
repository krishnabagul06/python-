import array as arr
a=arr.array('i',[10,20,30])
b=arr.array('i',[40,50,60])
a.extend(b)
print(a)