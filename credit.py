import pandas as pd
cc = input("please add your credit card number:")
cc = int(cc)

while cc <= 0:
    cc = input("Retry:")
    cc = int(cc)
#123456789101112131415
#3714496353 9 8 4 3 1
cc_str = list(map(int, str(cc)))
for x in str(cc_str):
    x_back = cc_str[len(cc_str):0:-1]
    x_back_select = x_back[1::2]
    x_multiply = [x * 2 for x in x_back_select]
    x_sum = sum(int(char) for n in x_multiply for char in str(n))
    x_forward = cc_str[0::2]
    check_cc = x_sum + sum(int(char) for n in x_forward for char in str(n))
    print(check_cc)
