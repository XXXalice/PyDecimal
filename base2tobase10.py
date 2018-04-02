
def calc_base2(base2_list):
    base2_list = reversed(base2_list) #ひっくり返さんとイカン
    base10 = 0
    index = 1
    for num in base2_list:
        if num == 1:
            base10 += index
        index *= 2

    return base10


# if __name__ == '__main__':
#     base2 = input()
#     try:
#         base2_list = list(map(int, list(base2)))
#     except:
#         print('please input only integer.')
#         exit(0)
#     print(calc_base2(base2_list))