s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
s1num=s1[1:]
s2num=s2[1:]
s3num=s3[1:]

name=input("Enter student's name:  ")
if name==s1[0]:
    print(name, sum(s1num))
elif name==s2[0]:
    print(name, sum(s2num))
elif name==s3[0]:
    print(name, sum(s3num))
else:
    print('Student is not recorded  0 ')
