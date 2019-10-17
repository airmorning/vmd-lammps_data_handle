file_path1='C:\\Users\\yinhang\\Desktop\\1.data'
file_path2='C:\\Users\\yinhang\\Desktop\\2.data'
lines = []

with open(file_path1,'r') as file_origin:
    lines = file_origin.readlines()


flag = False
res = []
for line in lines:
    if 'Bonds' in line:
        break
    if " Atoms # full" in line:
        flag = True
        continue
    if flag:
        number = line.strip('\n').split(" ")
        res.append(number)
del res[0]
del res[-1]
atoms=len(res)
# print(res)
# print(atoms)
i=0
x=[]
y=[]
z=[]

while i<=atoms-1:
    # print(res[i][4])
    x.append(float(res[i][4]))
    y.append(float(res[i][5]))
    z.append(float(res[i][6]))
    i=i+1
max_x=max(x)+0.5
min_x=min(x)-0.5
max_y=max(y)+0.5
min_y=min(y)-0.5
max_z=max(z)+0.5
min_z=min(z)-0.5
# print(x)
# print(y)
# print(z)
# print(max_x,min_x,max_y,min_y,max_z,min_z)
with open(file_path2,'w') as file_result:
    for line_1 in lines:
        if '-0.500000 0.500000  xlo xhi' in line_1:
            line_1 = ' '+str(min_x)+" "+str(max_x)+' xlo xhi\n'
        if '-0.500000 0.500000  ylo yhi' in line_1:
            line_1 = ' '+str(min_y)+" "+str(max_y)+' ylo yhi\n'
        if '-0.500000 0.500000  zlo zhi' in line_1:
            line_1 = " "+str(min_z)+" "+str(max_z) + ' zlo zhi\n '
        if 'bonds' in line_1:
            line_1 = '\n'
        if '0 angles' in line_1:
            continue
        if ' 0 dihedrals' in line_1:
            continue
        if ' 0 impropers' in line_1:
            continue
        if '1 bond types' in line_1:
            line_1='\n'
        if '0 angle types' in line_1:
            continue
        if '0 dihedral types'in line_1:
            continue
        if '0 improper types' in line_1:
            continue
        if 'Bonds' in line_1:
            break
        print(line_1.rstrip())

        file_result.write(line_1)




