# from numpy import append

# num = []
# for i in range(100): 
#     if i%2==1: 
#         num.append(i)
#         i+=1
# print(num)
_list = [i**2 for i in range(1,100) if i%2 != 0]
print(_list)