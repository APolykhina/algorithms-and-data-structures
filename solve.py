import vector_of_values
import check


def check_vector(str):
    for i in range(len(str)):
        if (str[i] != "1") and (str[i] != "0"):
            return "error"
    size = len(str)
    while size != 1:
        if size % 2 == 0:
            size = size / 2
        else:
            return "error"
    return "ok"


def check_function(bul_func):
    rez = "(" + bul_func.get_vector() + ")\n"
    rez = rez + "T0 - "
    if check.check_class_T0(bul_func) == 0:
        rez = rez + "не принадлежит \n"
    else:
        rez = rez + "принадлежит \n"
    rez = rez + "T1 - "
    if check.check_class_T1(bul_func) == 0:
        rez = rez + "не принадлежит \n"
    else:
        rez = rez + "принадлежит \n"
    rez = rez + "S - "
    if check.check_class_S(bul_func) == 0:
        rez = rez + "не принадлежит \n"
    else:
        rez = rez + "принадлежит \n"
    rez = rez + "M - "
    if check.check_class_M(bul_func, [0, bul_func.get_size() // 2 - 1], [bul_func.get_size() // 2, bul_func.get_size() - 1]) == 0:
        rez = rez + "не принадлежит \n"
    else:
        rez = rez + "принадлежит \n"
    rez = rez + "L - "
    if check.check_class_L(bul_func) == 0:
        rez = rez + "не принадлежит \n"
    else:
        rez = rez + "принадлежит \n"
    return rez


def solve(input, output):
    for line in input:
        if check_vector(line) == "ok":
            vector = vector_of_values.the_vector_of_values(line)
            output.write(check_function(vector))
        else:
            output.write("error")