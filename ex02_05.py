so_gio_lam = float(input("Nhập số giờ làm mỗi tuần :"))
muc_luong = float(input("Nhập mức lương :"))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam-gio_tieu_chuan)
thuc_linh = gio_tieu_chuan* muc_luong + gio_vuot_chuan* muc_luong *1.5
print("Sô tiền được lĩnh" , thuc_linh)