#This program can sort any list of numbers using 'swap sort'
#by craig kost
#date: 1/9/2022

#functions to run the program are at the bottom

import random

def ul_get(num):
    list = []
    for i in range(1,num):
        list.append(random.randrange(1,num))
    return list

def swap_sort_verbose(ul):
    steps = 0
    original_list = ul[:]

    for i in range (0,len(ul)):
        print("i: ",i)
        x=i+1
        steps += 1
        while x < len(ul):
            steps += 1
            print("x: ",x)
            base_num = ul[i]
            comp_num = ul[x]
            print("base num: ",base_num)
            print("comp num: ",comp_num)
            if ul[i] > ul[x]:
                ul[i] = comp_num
                ul[x] = base_num
                print ("Swapped: ",comp_num, " and ",base_num)
                print ("New UL: ",ul)
                x=i+1
            else:
                x = x+1
                print ("No Swap")

    print('Original List')
    print(original_list)
    print('New List')
    print(ul)
    print('total steps: ',steps)

def swap_sort(ul):
    steps = 0
    original_list = ul[:]
    for i in range (0,len(ul)):
        x=i+1
        steps +=1
        while x < len(ul):
            steps += 1
            base_num = ul[i]
            comp_num = ul[x]
            if ul[i] > ul[x]:
                ul[i] = comp_num
                ul[x] = base_num
                x=i+1
            else:
                x = x+1
    print('Original List')
    print(original_list)
    print('New List')
    print(ul)
    print('total steps: ',steps)


#run the program in here
for i in range(2): #change this to run multiple lists eg (range(2) will run 2 lists)
    ul = ul_get(10) #changes the length of the list eg (ul_get(10) does a 10 number list)
    #swap_sort_verbose(ul) #run verbose version that prints a ton of neat stuff
    swap_sort(ul) #run without the verbosity
