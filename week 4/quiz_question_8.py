user_num = int(input("Ente an number: "))
num = 1
while num <= user_num:
    if user_num % num ==0:
        print(num, end=" ")
    num += 1
