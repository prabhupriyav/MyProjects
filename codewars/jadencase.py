def to_jaden_case(string):
    str1 = ''
    list1 = []
    list2 = []
    string1 = string.split(" ")
    for i in string1:
        if string1[0] == i:
            str1= str1 + (i.capitalize())
        else:
            if i[-1] == 'i':
                print('inside i check')
                list1 = i.split('i')
                if list1[0] != ' ':
                    print('if 1')
                    str1= str1 + " " +(list1[0].capitalize())
                    str1= str1 + ' ' + ('I')
                else:
                    print('else 1')
                    str1= str1 + ' ' + (list1[0].capitalize())
                    str1= str1 + ' ' + ('I')
            elif  i[-3::] == 'you':
                print('inside you check')
                list1 = i.split('you')
                if list1[0] != ' ':
                    print('if 2')
                    str1= str1 + ' ' + (list1[0].capitalize())
                    str1= str1 + ' ' + ('You')
                else:
                    print('else 2')
                    str1= str1 + ' ' + (list1[0].capitalize())
                    str1= str1 + ' ' + ('You')
            else:
                str1= str1 + ' ' + (i.capitalize())
    
    return str1
to_jaden_case('you can discover everythingyou need to know about everything by looking at your hands')
