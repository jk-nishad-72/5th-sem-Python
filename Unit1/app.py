
list = [1, 2, 3, 4, 5]
userList = input("Enter numbers separated by space: ") 
print("User Input List: ", userList)
list = [int(x) for x in userList.split()]
print("Converted List: ", list)

def list_sum(input_list):
    sum = 0
    for element in input_list:
        sum += element
    return sum 

# print('Sum of list :',list_sum(list)) 
# checking the membership opearator 
def check_memberShip(input_list , element):
    if element in input_list:
        return True
    else:
        return False
# element = int(input("Enter element to check membership: "))
# print('Is '+ str(element) +' Exists in list :',check_memberShip(list,element)) 

def check_elementNotInlist(input_list , element ):
    if element not in input_list:
        return True
    else:
        return False

# print('Is ' + str(element) + ' Not Exists in list :',check_elementNotInlist(list,element)   )


#  list and tuple  and set

# list 
list1 = [30 , 500 , 10 ,2  ,3 , 4 , 5  ]
#  list characterstics 

list1[2] = 4
list1.pop()
# list1.clear()
list1.append(100) 
list1.sort()


# set 
set = { 1 , 1 , 2 ,3 }
set.add(500)
set.add(1000)
set.remove(2)

# tuple 
tuple1  = (1 ,2 , 3, 4 , 5 )

# tuple1[0] = 10

# print(f"List : {list1 } , lenght ->{len(list1) , len(tuple1) , len(set)}! Tuple : {tuple1} ! set :{set}")

#  file handling
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    
# Reading from a file
with open("example.txt","r") as f :
    content = f.read()
    print(f"\n File Content:\n {content}")


    


