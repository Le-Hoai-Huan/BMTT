def truy_cap_phan_tu (tuple_data):
    chuoi_dau = tuple_data[0]
    chuoi_cuoi = tuple_data[-1]

    return chuoi_dau,chuoi_cuoi

nhap_tuple = eval(input("Nhập tuple : "))
dau, cuoi = truy_cap_phan_tu(nhap_tuple)

print("Phần tử đâì tiên",dau)
print("Phần tử cuối cùng ", cuoi)