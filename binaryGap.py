decimal = input("decimal: ")
binary = bin(int(decimal))
binary = binary[2:]
bin1 = bin(1)
bin0 = bin(0)
# print(bin0, bin1)
firstOne = -1
count = 0

for i in range(0, len(binary)):
    print("i first: ", i)
    temp = 0
    if binary[i] == '1':
        flag = False
        while i <= len(binary)-2 :
            if binary[i+1] == '1':
                flag = True
                break
            else:
                temp += 1
                i += 1
        if not flag:
            break
        else:
            if temp > count:
                count = temp
        print("i last: ", i)
        print("temp: ", temp)




print("count: ", count)

print(binary) #, binary[0], binary[1], len(binary))

# 10100