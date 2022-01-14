def ktthuannghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;

hoten=str(input("Nhập họ và tên: "));
print

ho=str(input("Nhập họ: "));
tendem=str(input("Nhập tên đệm: "));
ten=str(input("Nhập tên: "));
n=str(len(ho))+str(len(tendem))+str(len(ten));

if(ktthuannghich(n)==True):
    print(n , "là số thuận nghịch");
else: print(n, "không phải là số thuận nghịch");