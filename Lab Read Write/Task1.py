Xnum1 = input()  #รับค่า input จากผู้ใช้

with open(r"C:\Users\CSIT\Desktop\pui1.txt", "w+") as file:
    file.write(Xnum1)  # เขียนข้อมูลที่ได้รับไปยังไฟล์
    file.seek(0)  # กลับไปที่ตำแหน่งเริ่มต้นของไฟล์
    Xnum2 = file.read()  # อ่านค่าจากไฟล์
num = int(Xnum2)  # แปลงข้อมูลจากไฟล์เป็นตัวเลข

if num % 2 != 0:  
    if num > 10:
        result = num + 10  #ถ้าเป็นเลขคี่และมากกว่า 10 ให้บวก 10
    else:
        result = num - 8  #ถ้าเป็นเลขคี่แต่ไม่เกิน 10 ให้ลบ 8
    print(result)
else:
    print("ไม่ใช่เลขคี่")
