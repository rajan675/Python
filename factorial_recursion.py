def facotrial_recursive(n):
        if n==0 or n==1:
            return 1
        return n* facotrial_recursive(n-1)
f= facotrial_recursive(5)
print(f)

def facotrial_iterate(n):
        if i in range(n):
            if n==0 or n==1:
                return 1
            else:       
                return n* facotrial_iterate(i+1)
f= facotrial_recursive(5)
print(f)

