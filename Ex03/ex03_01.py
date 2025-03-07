def tinh_tong_chan (n) :
    tong = 0
    for so in n :
        if so %2 ==0 :
            tong += so
            return  tong
nhap_chuoi = input("Nhập danh sách các số :")
so_Nhieu = list(map(int, nhap_chuoi.split(',')))

tong_chan = tinh_tong_chan(so_Nhieu)
print("Tổng số chẵn trong list là :", tong_chan)
