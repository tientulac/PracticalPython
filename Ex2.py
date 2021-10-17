#Hãy viết chương trình cho phép nhập vào một số xâu ký tự và cho biết số ký tự đã sử dụng trong mỗi xâu. Yêu cầu sử dụng hàm.
#Phân tích
#1.	Bài toán yêu cầu nhập vào một số xâu ký tự mà không cho biết số lượng cụ thể. 
# Do đó, khi viết hàm tính toán số ký tự nhận các xâu này làm tham số, chúng ta cần sử dụng tham số biến động *args 
#2.	Nói đến tính chất không trùng lặp, chúng ta nghĩ đến việc sử dụng set. 
# Như vậy, việc tìm các ký tự không trùng lặp được biến đổi thành việc chuyển một xâu thành set, khi đó các ký tự trùng lặp sẽ tự động được loại bỏ.
#3.	Số ký tự được sử dụng trong mỗi xâu chính là số phần tử của set thu được ở bước 2.

import unidecode
#Ham xoa dau Tieng Viet
def remove_accent(text):
    return unidecode.unidecode(text)

def count_character(text):
    set_char = set()
    for c in remove_accent(str(text).lower()):
        set_char.add(str(c))
    print("Tong so ky tu co trong xau (bao gom ca khoang trang) la: {}".format(str(len(set_char))))
    for rs in set_char:
        print(str(rs))
str_input = str(input("Nhap ho va ten tu ban phim: \n"))
count_character(str_input)