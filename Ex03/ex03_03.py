def tao_tuple_tu_chuoi(n):
    return tuple(n)
nhap_chuoi = input("Nhập danh sách các số")
so_Nhieu = list(map(int,nhap_chuoi.split(',')))
my_tuple = tao_tuple_tu_chuoi(so_Nhieu)
print("Chuỗi :",so_Nhieu)
print("Tuple từ chuỗi :", my_tuple)