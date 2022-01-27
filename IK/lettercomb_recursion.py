def letterCombinations(digits):
        dict1 = {"1":'',"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],
                 "5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r','s'],
                 "8":['t','u','v'],"9":['w','x','y','z']}
        #digit1 = list(digits)
        res = []
        def rec_fn(digits,pos,temp):
            if not digits:
                return res
            elif pos == len(digits):
                if len(temp) > 0:
                    res.append("".join(temp))
                    
            else:
                for j in dict1[digits[pos]]:
                    temp.append(j)
                   # print(temp)
                    rec_fn(digits,pos+1,temp)
                    temp.pop()
        rec_fn(digits,0,[])
        return res

letterCombinations("23")
