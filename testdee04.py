#Function 4 : Have Parameter/Have Return ***

def A(x,y):
    print(f"x is {x}")
    print(f"y is {y}")
    return x + y

def B(x,y):
    return f"Hi {x}", 2023 - y

print(f"Sum is {A(10 ,20)}")

g ,u = B("สมหญิง", 2000)
print(f"{g} อายุ {u} ปี")