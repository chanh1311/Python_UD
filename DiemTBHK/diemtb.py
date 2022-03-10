sotinchi = 0
diemso = 0
sum = 0
while True:
    print("Nhap vao diem chu:")
    diemchu = input()
    if (
        diemchu != "A"
        or diemchu != "B+"
        or diemchu != "B"
        or diemchu != "C+"
        or diemchu != "C"
        or diemchu != "D+"
        or diemchu != "D"
        or diemchu != "F"
    ):
        # print(round(sum / sotinchi), 1)
        break
    print("Nhap vao so tin chi cua mon hoc:")
    tinchi = int(input())
    if diemchu == "A":
        diemso = 4.0
    elif diemchu == "B+":
        diemso = 3.5
    elif diemchu == "B":
        diemso = 3.0
    elif diemchu == "C+":
        diemso = 2.5
    elif diemchu == "C":
        diemso = 2.0
    elif diemchu == "D+":
        diemso = 1.5
    elif diemchu == "D":
        diemso = 1.0
    elif diemchu == "F":
        diemso = 0.0

    sum += diemso * tinchi
    sotinchi += tinchi
