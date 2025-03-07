input_str = input("Nhập x,y:")
kick_thuoc = [int(x) for x in input_str.split(',')]
soHang  = kick_thuoc[0]
soCot = kick_thuoc[1]
nhieuHang = [[0 for cot in range (soCot)] for hang in range(soHang)]
for hang in range (soHang):
    for cot in range(soCot):
        nhieuHang[hang][cot]  = hang*cot
        print(nhieuHang)