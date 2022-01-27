user_name = input('Please Enter your Name : ')
user_food = input('What is your favorite food : ')

with open('./aboutme.txt', 'a') as file_object:
    #file_object.write(user_name + ' Favorite food is ' + user_food + '\n')
    file_object.write(f' hi {user_name}  your favorite food is {user_food} \n')
