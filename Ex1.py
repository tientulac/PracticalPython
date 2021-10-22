#Viết chương trình yêu cầu nhập vào họ tên một người và thực hiện các công việc sau:
#a.	Cho biết trong họ tên vừa nhập có chứa từ ”An” hay không? Nếu có thì xuất hiện bao nhiêu lần?
#b.	Cho biết người đó có phải tên là Anh hay không?
#Ví dụ: Họ tên là “Nguyen Thi Van”, trong họ tên vừa nhập có chứa từ ‘an’, nhưng tên không phải là “Anh”. Tên là “Van”.


import unidecode
#Ham xoa dau Tieng Viet
def remove_accent(text):
    return unidecode.unidecode(text)


#Nguoi dung nhap ten tu ban phim
name_input = str(input("Nhap ho va ten tu ban phim: \n"))
_name = remove_accent(name_input.lower())
name_check = "An".lower()

check_count = _name.count(name_check)

if check_count > 0:
    print(
        "+) Ten ban vua nhap co chua tu an \n+) So lan xuat hien la {} ".format(str(check_count))
    )
    arr_splitName = _name.split(" ")
    last_name = arr_splitName.pop().lower()
    if last_name == "Anh".lower() :
        print("Nguoi ban vua nhap ten la Anh")
    elif (name_check in last_name and last_name != "Anh".lower()) :
        print(
            "Ho ten ban vua nhap co tu an, nhung ten khong phai la anh, ten la {} \n".format(str(last_name.upper()))
        )
    else:
        print("Ho ten ban vua nhap co tu an, nhung ten la {} \n".format(str(last_name.upper())))
else :
    print("Ten ban vua nhap khong co tu An")


