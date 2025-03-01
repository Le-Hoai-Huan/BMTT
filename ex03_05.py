def dem_so_lan_xuat_hien(n):
    count_dict ={}
    for item in n :
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item] = 1
    return count_dict
nhap_chuoi = input("nhập danh sách các từ ")
word_list = nhap_chuoi.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử :", so_lan_xuat_hien)