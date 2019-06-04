
l = []
w = ''
def f(w,c,l,i,size,parameter):
	w += c
	if i == size :
		l = l.append(w)
		return w
	for j in range(parameter):
		f(w,str(j),l,i+1,size,parameter)

f(w,'',l,0,3,3)

print("shows repeated permutation: ")
print(l)
