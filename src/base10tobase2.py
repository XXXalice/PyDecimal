
def calc_base10(base10):
    base2_list = []
    while(base10 >= 1):
        bit = base10 % 2
        base2_list.append(bit)
        base10 /= 2
        base10 = int(base10)
    base2 = ''.join(map(str,reversed(base2_list)))

    return base2


# if __name__ == '__main__':
#     base10 = int(input())
#     print(calc_base10(base10))