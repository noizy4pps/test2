def parla(s: str):
    print(s)

def conta(n1: int, n2: int, op: str):
    res = 0
    if op == "+":
        res = n1 + n2
    elif op == "-":
        res = n1 - n2
    
    print("result=", res)
    return res
    