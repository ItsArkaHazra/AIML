# 1
# 123
# 12345
# 1234567
# 123456789

inputrange=int(input("Enter Range Of *: \n"))
print("\n\n\n\nOutput-----------------------\n\n\n")
for i in range(1,inputrange+1,1):
    text='Line '+str(i)+'= '  
    for j in range(1,i+1,1):
        text=text+str(j)+' '
    print(text)
