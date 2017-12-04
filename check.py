def check_class_T0(bul_func):
    return bul_func.get_bit(0) == 0


def check_class_T1(bul_func):
    return bul_func.get_bit(bul_func.get_size() - 1) == 1


def check_class_S(bul_func):
    if (check_class_T0(bul_func) and check_class_T1(bul_func) == 0) or (check_class_T0(bul_func) == 0 and check_class_T1(bul_func)):
        return False
    for i in range(bul_func.get_size() // 2):
        if bul_func.get_bit(i) == bul_func.get_bit(bul_func.get_size() - i - 1):
            return False
    return True


def comparision_of_vectors(bul_func, start1, start2, step):
    for i in range(step):
        if bul_func.get_bit(i + start1) > bul_func.get_bit(i + start2):
            return False
    if step != 1:
        if comparision_of_vectors(bul_func, start1, start1 + step // 2, step // 2) == 0:
            return False
        if comparision_of_vectors(bul_func, start2, start2 + step // 2, step // 2):
            return True
        else:
            return False
    return True


def check_class_M(bul_func):
    return comparision_of_vectors(bul_func, 0, bul_func.get_size() // 2, bul_func.get_size() // 2)


def sum_mod_2(ch1, ch2):
    if (ch1 == 1 and ch2 == 1) or (ch1 == 0 and ch2 == 0):
        return 0
    else:
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
            value_list[deg - current_deg] = sum_mod_2(value_list[0], int(bul_func.get_bit(i)))
            current_deg = current_deg + 1
        else:
            rez = sum_mod_2(value_list[0], int(bul_func.get_bit(i)))
            num_of_x = deg
            x = i
            while x != 0:
                if x & 1:
                    rez = sum_mod_2(rez, value_list[num_of_x])
                num_of_x = num_of_x - 1
                x = x >> 1
            if rez:
                return False
    return True