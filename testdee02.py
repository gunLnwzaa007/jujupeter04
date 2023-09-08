#Function 2 : Have Parameter/No Return
#Parameter คือ ตัวเเปรประเภทหนึ่ง ขอบเขตการใฃ้งานพารามิเตอร์
#จะใช้ได้เฉพาะในฟังก์ฃันนั้นๆ เท่านั้น

def A(x,y) :
    print("haa")
    z = x + y
    print(f"{x} + {y} = {z}")
    #ไม่มีคำสั่ง retrun

def B( x ) :
    print(f"X is {x} 555...")

A(10,20) #Argument อากิวเมนต์(ข้อมูลทีี่ส่งไปให้ parameter)Ex A(5,2)=2
A(5,5)
B("รักนะจ๊ะ")