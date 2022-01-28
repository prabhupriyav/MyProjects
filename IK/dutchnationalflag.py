def dutch_flag_sort(balls):

    lenballs = len(balls)
        i=0
        r=-1
        g=-1    
    while i < lenballs:
        if balls[i] == 'G':
            g+=1
            balls[i],balls[g] = balls[g],balls[i]
        elif balls[i] == 'R':
            g+=1
            balls[i],balls[g] = balls[g],balls[i]
            r+=1
            balls[r],balls[g] = balls[g],balls[r]
        i+=1
    return balls
