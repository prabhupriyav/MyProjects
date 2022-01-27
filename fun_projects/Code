
## david@outco.io

# 
# majority_element_top_two
#  
# Write a function which accepts an array of integers and returns in a new two item array
# the two integers in the input that appear most frequently.
# 
# majority_element_top_two([3,3,1,2,1,1,4,4,4,4]); ==> [4,1]
#                                             i
# counts = {'3': '2', '1': '3', '2':'1', '4': '4'}
#                           creating empty list
# for every item in the array
# 
#


def majority_element_top_two(array):
   max_val = []
   dict_count= {}
   for i in array:
       ## conditiion 1: check to see if we've seen the element
          ## add 1 to existing count
       if i in dict_count:
         dict_count[i] = dict_count[i] + 1
       ## condition 2: element has not been seen before
          ## create new key and set value to be 1
       else: 
         dict_count[i] = 1
   dict_temp = dict_count.copy()   
   
   for j,k in dict_count.items(): 
            
          temp = max(dict_temp.values())
        
          temp1 = [l for l,m in dict_temp.items() if m == temp]
        
          max_val.append(temp1[0])
          
          del dict_temp[temp1[0]]
          if len(max_val) == 2:
              break
          else:
              continue 
     
   return(max_val)      
     
     
print(majority_element_top_two([3,3,1,2,1,1,4,4,4,4]))   
     

