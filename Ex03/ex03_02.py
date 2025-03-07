def dao_nguoc_list (n):
    return n[::-1]

nhap_chuoi = input("Nhập danh sách các số")
so_Nhieu = list(map(int , nhap_chuoi.split(',')))

chuoi_dao_nguoc = dao_nguoc_list(so_Nhieu)
print("Chuỗi sao khi đảo ngược :", chuoi_dao_nguoc)