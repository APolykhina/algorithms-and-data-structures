import vector_of_values
import check


def check_vector(str):
    for i in range(len(str)):
        if (str[i] != "1") and (str[i] != "0"):
            return False
    size = len(str)
    return (size != 0) and ((size & (~size + 1)) == size)


def check_function(bul_func):
    rez = "(" + bul_func.get_vector() + ")\n"
    temp = [
        ('T0', check.check_class_T0(bul_func)),
        ('T1', check.check_class_T1(bul_func)),
        ('S', check.check_class_S(bul_func)),
        ('M', check.check_class_M(bul_func)),
        ('L', check.check_class_L(bul_func)),
    ]
    for name, rezult in temp:
        rez = rez + '{} - {}'.format(name, 'принадлежит \n' if rezult == 1 else 'не принадлежит \n')
    return rez


def solve(input, output):
    for line in input:
        if check_vector(line):
            vector = vector_of_values.the_vector_of_values(line)
            output.write(check_function(vector))
        else:
            output.write("error")