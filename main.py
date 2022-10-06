import random
import time

t1 = 0 
t2 = 0

def measure_time():
  milliseconds = int(round(time.time() * 1000))
  #print(milliseconds)
  return milliseconds

# Python3 code to iterate over a list
list = [3.3,2.1,2.22,6.7,8.9,3.0]
list1 = []
length = 0 
tmp = 0
# Using for loop
def print_array(tmplist):
  for i in tmplist:
	  print(i)
  print("=======")


def generate_data():
  f = open("demofile2.txt", "w")
  for i in range(5000):
    num = random.randint(1,3000)
    f.write(str(num))
    f.write("\n")
    print (num)
  f.close()

def load_data():
  length1 = len(list1)
  with open('demofile2.txt') as f:
    for line in f:
      #print (line)
      list1.insert(0,int(line))
  
def bubble_sort_array(tmplist):
  length = len(tmplist)

  for j in range(length-1):
    for i in range(length-1):
      if tmplist[i] > tmplist[i+1]:
        tmp = tmplist[i]
        tmplist[i] = tmplist[i+1]
        tmplist[i+1] = tmp



def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
def quick_sort_array(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quick_sort_array(l, pi-1, nums)  # Recursively sorting the left values
        quick_sort_array(pi+1, r, nums)  # Recursively sorting the right values
    return nums



#print_array(list)
#t1 = measure_time()
#bubble_sort_array(list)
#t2 = measure_time()
#print_array(list)
#print ("Total Execution Time: ", (t2-t1)," ms")


generate_data()
load_data()
print_array(list1)
t1 = measure_time()
#bubble_sort_array(list1)
quick_sort_array(0,len(list1)-1,list1)
t2 = measure_time()
print_array(list1)
print ("Total Execution Time: ", (t2-t1)," ms")
