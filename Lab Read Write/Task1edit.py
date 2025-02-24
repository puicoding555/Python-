num=int(input())

with open(r"C:\Users\CSIT\Desktop\pui1.txt", "w+") as file:
    file.write(str(num))
    file.seek(0)
    num=int(file.read().strip())
print(num + 10 if num % 2 != 0 and num > 10 else num - 8)