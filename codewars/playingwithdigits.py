def dig_pow(n, p):
    orgp = p
    power1 = str(n)
    total = 0
    for i in power1:
        inti = int(i)
        powerval = ((inti ** p))
        total = total + powerval
        p+=1
    count = (total // n)
    if count > 1:
        return count
    else:
        return -1
    
       
dig_pow(9400,1)
