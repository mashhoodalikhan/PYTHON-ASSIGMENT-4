list=[1,2,2,2,6.7,8,9,8,6,5]
unique_list=[]
for a in list:
     if a not in unique_list:
          unique_list.append(a)
print(unique_list)