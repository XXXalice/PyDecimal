class PyDecimal:
    def __init__(self):
        pass

    def calc_base2(self,base2_list):
        base2_list = reversed(base2_list)  # ひっくり返さんとイカン
        base10 = 0
        index = 1
        for num in base2_list:
            if num == 1:
                base10 += index
            index *= 2

        return base10

    def calc_base10(self, base10):
        base2_list = []
        while (base10 >= 1):
            bit = base10 % 2
            base2_list.append(bit)
            base10 /= 2
            base10 = int(base10)
        base2 = ''.join(map(str, reversed(base2_list)))

        return base2