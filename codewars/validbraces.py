def validBraces(string):
    n = 1
    result = True
    for i in range(0,len(string),n):
      #  print(string[i], string[i+n])
        if (string[i] == '('):
            print('in first string')
            print(i)
            if (string[i+n] == ')'):
                result = True
            else: 
                result = False
                print(i)
                if i >= len(string):
                     break
            print(result)
        elif (string[i] == '{'): 
            print('in second string')
            print(i)
            if (string[i+n] == '}'):
                print('in second string -1')
                print(i)
                result = True
            else:
                result = False
                print(i)
                if i >= len(string):
                     break
        elif (string[i] == '['):
            if (string[i+n] == ']'):
                result = True
            else:
                result = False
                print(i)
                if i >= len(string):
                     break
        
    return result
validBraces("(((({{")
