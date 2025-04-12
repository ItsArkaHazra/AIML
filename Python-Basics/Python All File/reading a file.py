file=open('demo.txt','r') 
for line in file:
    print(line)
str1=file.read(10)
print(str1)
str2=file.read(40)
print(str2)

str=file.read()
print(str)
print(file)

str1=file.readline()
str2=file.readline(2)
str3=file.readline()
print(str1)
print(str2)
print(str3)

lines=file.readlines()
for i in lines:
    print(i)

print(len(lines))



