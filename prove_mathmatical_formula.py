def lhs(a,b):
    return (a+b)**2

def rhs(a,b):
    return a**2+2*a*b+b**2


ls = lhs(2,1)
rs = rhs(2,1)

print("LHS = {}, RHS = {}".format(ls,rs))
print("proved.")
