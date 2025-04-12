# 	1	2	3	4	5	6	7	8	9	10	11	12	13
# 1	*	*	*	*	*	*	*	*	*	*	*	*	*
# 2	*	*	*	*	*	*	*	*	*	*	*	*	
# 3	*	*	*	*	*	*	*	*	*	*	*		
# 4	*	*	*	*	*		*	*	*	*			
# 5	*	*	*	*	*	*	*	*	*				
# 6	*	*	*	*	*	*	*	*					
# 7	*	*	*	*	*	*	*						
# 8	*	*	*	*	*	*							
# 9	*	*	*	*	*								
# 10	*	*	*	*									
# 11	*	*	*										
# 12	*	*											
# 13	*												


r=int(input("Enter Range Of *: \n"))
test=''


print("\n\n\n\nOutput-----------------------\n\n\n")
for i in range(r,0,-1):
    test='Line '+str(i)+'= '  
    for j in range(1,i+1):
        test=test+"* "
    print(test)



