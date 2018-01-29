def stamps(n):
    # Your code here
    c1 = 5
    c2 = 2
    c3 = 1
    c1_n = n//c1
    c2_n = n%c1 //c2
    c3_n = n%c1%c2/c3
    return c1_n, c2_n, c3_n


print(stamps(8))