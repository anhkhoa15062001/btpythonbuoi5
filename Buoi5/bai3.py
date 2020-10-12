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
def tim_max(n):
    n=input_list(n)
    max = n[0]
    for i in range(1,len(n)):
        if(max<n[i]):
            max=n[i]
    return max
n=int(input("Nhap: "))
print(input_list(n))
print(tim_max(n))