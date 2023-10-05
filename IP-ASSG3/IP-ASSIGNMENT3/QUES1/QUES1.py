n = int(input("Enter the value of n: "))
i = 2
def upper(n, m = 0):
    if n == 0: return
    print(n*"*" + 2*m*" " + n*"*")
    n-=1
    m+=1
    upper(n, m)

def lower(n):
    global i
    m = n - i
    if i == n + 1: return
    print(i*"*" + 2*m*" " + i*"*")
    i += 1
    lower(n)

upper(n)
#print()
lower(n)