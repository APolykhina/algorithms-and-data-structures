def check_class_T0(bul_func):
    if bul_func.get_bit(0) == 0:
        return 1
    else:
        return 0


def check_class_T1(bul_func):
    if bul_func.get_bit(bul_func.get_size() - 1) == 1:
        return 1
    else:
        return 0


def check_class_S(bul_func):
    if (check_class_T0(bul_func) and check_class_T1(bul_func) == 0) or (check_class_T0(bul_func) == 0 and check_class_T1(bul_func)):
        return 0
    for i in range(bul_func.get_size() // 2):
        if bul_func.get_bit(i) == bul_func.get_bit(bul_func.get_size() - i - 1):
            return 0
    return 1


def check_class_M(bul_func, first_part, second_part):
    for i in range(first_part[1] - first_part[0] + 1):
        if bul_func.get_bit(i + first_part[0]) > bul_func.get_bit(i + second_part[0]):
            return 0
    if first_part[1] - first_part[0] + 1 != 1:
        temp1 = check_class_M(bul_func, [first_part[0], (first_part[1] - first_part[0]) // 2 + first_part[0]], [(first_part[1] - first_part[0]) // 2 + first_part[0] + 1, first_part[1]])
        if temp1 == 0:
            return 0
        temp2 = check_class_M(bul_func, [second_part[0], (second_part[1] - second_part[0]) // 2 + second_part[0]], [(second_part[1] - second_part[0]) // 2 + second_part[0] + 1, second_part[1]])
        if temp2 == 1:
            return 1
        else:
            return 0
    return 1


def check_class_L(bul_func):
    value_list = dict()
    deg = 0
    size = bul_func.get_size()
    while size != 1:
        size = size // 2
        deg = deg + 1
    current_deg = 0
    for i in range(bul_func.get_size()):
        if i == 0:
            value_list[0] = int(bul_func.get_bit(0))
        elif i == pow(2, current_deg):
            if value_list[0] != 1:
                value_list[deg - current_deg] = int(bul_func.get_bit(i))
            else:
                if bul_func.get_bit(i) == 0:
                    value_list[deg - current_deg] = 1
                else:
                    value_list[deg - current_deg] = 0
            current_deg = current_deg + 1
        else:
            rez = int(bul_func.get_bit(i))
            if value_list[0] == 1:
                if rez == 1:
                    rez = 0
                else:
                    rez = 1
            x = bin(i)
            num_of_x = deg
            for j in range(len(x) - 1, -1, -1):
                if (j == 0) or (j == 1):
                    break
                if x[j] == '1':
                    if rez == 0:
                        rez = value_list[num_of_x]
                    else:
                        if value_list[num_of_x] == 1:
                            rez = 0
                        else:
                            rez = 1
                num_of_x = num_of_x - 1
            if rez == 1:
                return 0
    return 1