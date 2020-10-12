def input_data(n):
    arr=[]
    for i in range(n):
        x = int(input(f"Input item[{i}]: "))
        arr.append(x)
    return arr
def so_chan(arr):
    result = []
    for i in arr:
        if i%2==0:
            result.append(i)
    return result
n = int(input("Nhập phần tử :"))
arr = input_data(n)
print(arr)
print(so_chan(arr))
