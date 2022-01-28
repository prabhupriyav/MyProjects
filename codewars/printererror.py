def printer(string):
    str_comp = []
    count = 0
    len_string = len(string)
    valid_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    if string.isalpha() == True:
        for i in string:
            str_comp.extend(i)
        for j in str_comp:
            if j in valid_list:
                continue
            else:
                count += 1
        errors = 'count/len_string'
        answer = 'Printer errors ==> ' + str(count) +'/' + str(len_string)
        return answer
    else:
        print('String not valid')
        

printer("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
