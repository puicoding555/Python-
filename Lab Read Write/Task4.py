with open(r"C:\Users\CSIT\Desktop\PythonFile.txt", 'r') as file:
    content = file.read()
# ต่อท้ายคำว่า "ไพทอน"
content += " test"

# เขียนข้อมูลที่ได้ลงในไฟล์ "filePython_2.txt"
with open(r"C:\Users\CSIT\Desktop\filePython_2.txt", 'w') as file_2:
    file_2.write(content)
