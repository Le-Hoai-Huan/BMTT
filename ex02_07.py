dongs =[]
while True :
    dong = input()
    if dong.lower() == 'done':
        break
    dongs.append(dong)
    print("\n Các dòng đã nhập nsau khi chuyển thành chữ in hoa :")
    for  dong in dongs:
        print(dong.upper())