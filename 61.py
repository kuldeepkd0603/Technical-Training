# Print All Armstrong Numbers Between 1 and 999
def Armstrong():
    for i in range(1,1000):
        i=str(i)
        length=0
        power_sum=0
        for j in i:
            length=length+1
        for j in i:
            j=int(j)
            power_sum=power_sum+j**length
        
        