# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *

input=str(input("Enter Matric Size By Row(a) and Column(b) In the Form of aXb:\n"))
input=input.split('X')
a=int(input[0])
b=int(input[1])
for i in range(1,a+1,1):
    string=''
    for j in range(1,b+1,1):
        string=string+"* "
    string=string.strip()
    print(string)
