def kiem_tra_so_nguyen(n) :
    if n<= 1 :
        return  False
    for i in range (2 , int (n ** 0.5)+1):
        if n %i == 0:
            return  False
        return  True
so = int(input("Nhập vào số cần kiểm tra :"))
if kiem_tra_so_nguyen(so) :
    print(so ,"Là số nguyên tố")
else:
    print(so,"Không phải là số nguyên tố ")