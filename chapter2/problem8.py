def cumulative_sum(n):
    cum_sum = []
    y = 0
    for i in n:  
        y += i    
        cum_sum.append(y)
    print cum_sum
