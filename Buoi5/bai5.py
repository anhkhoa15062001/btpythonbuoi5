def input_data(n):
    arr=[]
    for i in range(n):
        x = int(input(f"Input item[{i}]: "))
        arr.append()
    return arr

def input_list(n):
    arr = []
    i = 0
    while True:
        x = input(f"Input item[{i}]: ")
        try:
            arr.append(int(x))
            i += 1
            if i >= n:
                break
        except:
            print("Chưa nhập đúng số nguyên. Nhập lại!")
    return arr
def so_le(n):
    n=input_list(n)
    result = []
    for i in n:
        if(i%2!=0):
            result.append(i)
        return result
n=int(input("Nhap: "))
print(input_list(n))
print(so_le(n))