#Function 3 : No Parameter/Have Return ***

def A():
    print("haa")
    print("hee")
    return "HOO HOO HOO"

def B():
    return 999, True, 10+20

# A() เขียนได้ เเต่เขาบ่ใช้กัน
print(A())

G = A() #ควรสร้างตัวเเปรเพื่อมาเก็บค่า Return

g, u, n =B()
print(f"{g}{u}{n}")



