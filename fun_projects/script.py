# print('hello')
#read a file
# text_fl = open('./text.txt')
# print(text_fl.read())
# text_fl.close()

#write a file

# text_fl = open('./text.txt','w')
# text_fl.write("hi there")
# text_fl.close()

#create a python file and write a python code
# text_file = open('./text2.py', 'w')
# text_file.write('def add(): \n')
# text_file.write('\t print(2 + 2) \n')
# text_file.write('add()')
# text_file.close()

#append in an existing text_file

# text_fl = open('./text.txt','a')
# text_fl.write("/n hi there new line")
# text_fl.close()

#with statement
# with open('./text.txt','a') as file1:
#     file1.write('helloege')
#     file1.close()

# with open('./text.txt','a') as file2:
#     file2.writelines('hi there \n i am here')
#     file2.close()

# with open('./text.txt') as file2:
#     print(file2.readlines())
#     file2.close()

#user input
user_input = input("What do u want to add:")
with open('./todo.txt', 'a') as file_object:
    file_object.write(user_input + '\n')
