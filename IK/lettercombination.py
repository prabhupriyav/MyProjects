def letterCombinations(digits):
        dict1 = {"1":'',"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],
                 "5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r','s'],
                 "8":['t','u','v'],"9":['w','x','y','z']}
        #digit1 = list(digits)
        if not digits:
            return []
        res = [""]
        for i in digits:
            temp = []
            for j in dict1[i]:
                for k in res:
                    temp.append(k+j)
            res = temp
        return res

letterCombinations("")
