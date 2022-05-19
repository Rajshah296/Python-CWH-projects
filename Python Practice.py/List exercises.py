                            # Exercise 1
# There are 2 lists list 1 and list 2,return a list which consists all the unique values of these 2 lists.

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,2,4,1,10]
list1.extend(list2)
list3 = []
for index,item in enumerate(list1):
    if item not in list3 :
        list3.append(item)
print(list3)
#                              Exercise - 2
# Transpose the matrix
matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix_2 = [[],[],[]]
for index1,item in enumerate(matrix_1) : 
    for index2,key in enumerate(item) : 
        matrix_2[index2].append(key)
print(matrix_2)

#                               Exercise - 3
# Square each item in the list and print it.

l1 = [1,2,3,4,5,6,7,8,9,10]
print([num ** 2 for num in l1])

#                               Exercise - 4 
# Combine all the corresponding string elements of the 2 given lists.

l2 = ['app','bo','co','doc']
l3 = ['le','y','ol','tor']
print([l2[index] + l3[index] for index,item in enumerate(l2)])

#                               Exercise - 5 
# Reverse the given list 

list1 = [1,2,3,4,5] # Input
list1 = list([list1[index] for index in range(len(list1) - 1,-1,-1)])
print(list1)

# Or

list1 = list1[::-1] # Negative index slicing
print(list1)

#                               Exercise - 6
# Input - [10,20,30,40],[Paddy,Ram.Bran,Andy]
# Output - [10 Andy,20 Bran, 30 Ram, 40 Paddy] 
list1,list2 = [10,20,30,40],["Paddy","Ram","Bran","Andy"]
for index,val in enumerate(list1) : 
    val = str(list1[index]) + " " + list2[::-1][index]
    list1[index] = val
print(list1)

#                             Exercise - 7 
list1 = [5,10,15,20,25,50,20] #Inp
# Replace 15 with 99
try : 
    list1[list1.index(15)] = 99
except :
    print("15 is not in the given list.")